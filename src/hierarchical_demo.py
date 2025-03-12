import os
from dotenv import load_dotenv
from crewai import Crew, Task
from langchain_openai import ChatOpenAI

# Import agents from different tiers
from src.agents.individual import (
    CTO_CAI,  # Tier 0
    TechnicalArchitectureManager,  # Tier 1
    AIResearchLead  # Tier 2
)

# Load environment variables
load_dotenv()

def main():
    """Main function to demonstrate hierarchical interaction between agents from different tiers."""
    
    # Initialize the language model
    llm = ChatOpenAI(
        model="o3-mini",  # Using o3-mini model as specified
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Initialize the agents
    ai_research_lead = AIResearchLead(llm=llm, verbose=True).to_agent()
    tech_arch_manager = TechnicalArchitectureManager(llm=llm, verbose=True).to_agent()
    cto_cai = CTO_CAI(llm=llm, verbose=True).to_agent()
    
    print("Initialized agents from all three tiers")
    
    # Create tasks for each agent in hierarchical order
    ai_research_task = Task(
        description="Identify three emerging AI technologies that could provide competitive advantage and briefly explain their potential applications",
        expected_output="A list of 3 emerging AI technologies with brief explanations",
        agent=ai_research_lead
    )
    
    tech_arch_task = Task(
        description="Review the AI Research Lead's findings and develop a preliminary technical architecture plan for implementing one of these technologies",
        expected_output="A preliminary technical architecture plan for one selected technology",
        agent=tech_arch_manager,
        context=[ai_research_task]  # This task depends on the AI Research Lead's output
    )
    
    cto_task = Task(
        description="Evaluate the Technical Architecture Manager's implementation plan and provide strategic guidance for integration with existing systems",
        expected_output="Strategic guidance for technology integration",
        agent=cto_cai,
        context=[ai_research_task, tech_arch_task]  # This task depends on both previous outputs
    )
    
    # Create a crew with the agents and tasks
    crew = Crew(
        agents=[ai_research_lead, tech_arch_manager, cto_cai],
        tasks=[ai_research_task, tech_arch_task, cto_task],
        verbose=True
    )
    
    # Run the crew
    print("Starting hierarchical crew execution...")
    result = crew.kickoff()
    
    print("\n==== Final Result ====\n")
    print(result)

if __name__ == "__main__":
    main()