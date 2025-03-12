import os
from dotenv import load_dotenv
from crewai import Crew, Task
from langchain_openai import ChatOpenAI

# Import specific agents
from src.agents.individual import Founder, CEO

# Load environment variables
load_dotenv()

def main():
    """Main function to demonstrate a quick interaction between two agents."""
    
    # Initialize the language model
    llm = ChatOpenAI(
        model="o3-mini",  # Using o3-mini model as specified
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Initialize the agents
    founder = Founder(llm=llm, verbose=True).to_agent()
    ceo = CEO(llm=llm, verbose=True).to_agent()
    
    print("Initialized Founder and CEO agents")
    
    # Create tasks for each agent
    founder_task = Task(
        description="Create a one-sentence vision for AI innovation",
        expected_output="A single sentence vision statement",
        agent=founder
    )
    
    ceo_task = Task(
        description="Based on the Founder's vision, list 3 key business initiatives",
        expected_output="A list of 3 key business initiatives",
        agent=ceo,
        context=[founder_task]  # The CEO's task depends on the Founder's output
    )
    
    # Create a crew with the agents and tasks
    crew = Crew(
        agents=[founder, ceo],
        tasks=[founder_task, ceo_task],
        verbose=True
    )
    
    # Run the crew
    print("Starting crew execution...")
    result = crew.kickoff()
    
    print("\n==== Final Result ====\n")
    print(result)

if __name__ == "__main__":
    main()