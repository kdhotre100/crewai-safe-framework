import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Import all agents
from src.agents.individual import all_agents

# Load environment variables
load_dotenv()

def main():
    """Test function to verify that agents can be initialized."""
    
    # Initialize the language model
    llm = ChatOpenAI(
        model="o3-mini",  # Using o3-mini model as specified
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Initialize all agents with the language model
    print("Initializing agents...")
    
    for i, agent_class in enumerate(all_agents):
        agent_name = agent_class.__name__
        print(f"{i+1}. Initializing {agent_name}...")
        agent = agent_class(llm=llm, verbose=True)
        print(f"   - Role: {agent.role}")
        print(f"   - Tier: {agent.tier}")
        print(f"   - Goal: {agent.goal}")
        print(f"   - Responsibilities: {len(agent.responsibilities)}")
        print(f"   - Meetings: {len(agent.meetings)}")
        print()
    
    print("All agents initialized successfully!")

if __name__ == "__main__":
    main()