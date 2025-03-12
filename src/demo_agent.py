import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Import the Founder agent
from src.agents.individual import Founder

# Load environment variables
load_dotenv()

def main():
    """Demo function to show a basic interaction with the Founder agent."""
    
    # Initialize the language model
    llm = ChatOpenAI(
        model="o3-mini",  # Using o3-mini model as specified
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Initialize the Founder agent
    founder = Founder(llm=llm, verbose=True)
    print(f"Initialized Founder agent: {founder.name}")
    print(f"Role: {founder.role}")
    print(f"Goal: {founder.goal}")
    print(f"Responsibilities:")
    for resp in founder.responsibilities:
        print(f"  - {resp}")
    print(f"Meetings:")
    for meeting in founder.meetings:
        print(f"  - {meeting}")
    print()
    
    # Generate a backstory for the agent
    backstory = founder._generate_backstory()
    print("Backstory:")
    print(backstory)
    print()
    
    # Demonstrate a simple interaction with the agent
    print("Asking the Founder agent about strategic vision...")
    
    # Create a system message with the agent's backstory
    system_message = SystemMessage(content=f"""
    You are the Founder of a technology company.
    {backstory}
    
    Please respond to the user's question in your role as the Founder.
    """)
    
    # Create a human message with a question
    human_message = HumanMessage(content="What is your strategic vision for AI innovation in the next quarter?")
    
    # Get a response from the language model
    response = llm.invoke([system_message, human_message])
    
    print("\nFounder's Response:")
    print(response.content)

if __name__ == "__main__":
    main()