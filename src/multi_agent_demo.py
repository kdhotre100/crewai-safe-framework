import os
from dotenv import load_dotenv
from crewai import Crew, Task
from langchain_openai import ChatOpenAI

# Import specific agents
from src.agents.individual import Founder, CEO, CTO_CAI

# Load environment variables
load_dotenv()

def main():
    """Main function to demonstrate multiple agents working together."""
    
    # Initialize the language model
    llm = ChatOpenAI(
        model="o3-mini",  # Using o3-mini model as specified
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Initialize the agents
    founder = Founder(llm=llm, verbose=True).to_agent()
    ceo = CEO(llm=llm, verbose=True).to_agent()
    cto_cai = CTO_CAI(llm=llm, verbose=True).to_agent()
    
    print("Initialized Founder, CEO, and CTO/CAI agents")
    
    # Create tasks for each agent
    founder_task = Task(
        description="Create a high-level strategic vision for AI innovation that aligns with Lean-Agile principles",
        expected_output="A concise strategic vision statement (1-2 paragraphs)",
        agent=founder
    )
    
    ceo_task = Task(
        description="Based on the Founder's strategic vision, develop a business plan that outlines key initiatives, resource allocation, and expected outcomes",
        expected_output="A business plan with key initiatives and resource allocation",
        agent=ceo,
        context=[founder_task]  # The CEO's task depends on the Founder's output
    )
    
    cto_cai_task = Task(
        description="Based on the Founder's vision and CEO's business plan, create a technical roadmap for implementing AI innovations in the next quarter",
        expected_output="A technical roadmap with specific AI implementation milestones",
        agent=cto_cai,
        context=[founder_task, ceo_task]  # The CTO's task depends on both previous outputs
    )
    
    # Create a crew with the agents and tasks
    crew = Crew(
        agents=[founder, ceo, cto_cai],
        tasks=[founder_task, ceo_task, cto_cai_task],
        verbose=True
    )
    
    # Run the crew
    print("Starting crew execution...")
    result = crew.kickoff()
    
    print("\n==== Final Result ====\n")
    print(result)

if __name__ == "__main__":
    main()