from src.agents.base_agent import BaseAgent
from langchain.schema import BaseLanguageModel

class TechnicalArchitectureManager(BaseAgent):
    """Technical Architecture & AI Strategy Manager agent."""
    
    def __init__(self, llm: BaseLanguageModel, verbose: bool = False):
        """Initialize the Technical Architecture & AI Strategy Manager agent.
        
        Args:
            llm: The language model to use for the agent.
            verbose: Whether to print verbose output.
        """
        super().__init__(
            llm=llm,
            name="Technical Architecture Manager",
            role="Technical Architecture & AI Strategy Manager",
            goal="Design and implement scalable technical architecture and AI enablers that support business objectives",
            tier=1,  # Operations & Strategy
            responsibilities=[
                "Design AI/tech enablers",
                "Enforce NFRs (e.g., scalability)",
                "Oversee architecture evolution"
            ],
            meetings=[
                "Tech Spike Planning",
                "Architectural Sync"
            ],
            verbose=verbose
        )