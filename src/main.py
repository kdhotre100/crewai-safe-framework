import os
from dotenv import load_dotenv
from crewai import Crew, Task
from langchain_openai import ChatOpenAI

# Import all agents
from src.agents.individual import all_agents

# Load environment variables
load_dotenv()

def main():
    """Main function to demonstrate the use of the agents."""
    
    # Initialize the language model
    llm = ChatOpenAI(
        model="o3-mini",  # Using o3-mini model as specified
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Initialize just the Founder agent for a simple test
    founder = all_agents[0](llm=llm, verbose=True).to_agent()
    
    print(f"Initialized Founder agent")
    
    # Create a simple task for the Founder
    founder_task = Task(
        description="Create a brief strategic vision statement for AI innovation",
        expected_output="A short strategic vision statement (1-2 paragraphs)",
        agent=founder
    )
    
    # Create a crew with just the founder and one task
    crew = Crew(
        agents=[founder],
        tasks=[founder_task],
        verbose=True
    )
    
    # Run the crew
    print("Starting crew execution...")
    result = crew.kickoff()
    
    print("\n==== Result ====\n")
    print(result)

if __name__ == "__main__":
    main()