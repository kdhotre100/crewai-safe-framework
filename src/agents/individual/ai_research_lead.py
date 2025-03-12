from src.agents.base_agent import BaseAgent
from langchain.schema import BaseLanguageModel

class AIResearchLead(BaseAgent):
    """AI Research Lead agent."""
    
    def __init__(self, llm: BaseLanguageModel, verbose: bool = False):
        """Initialize the AI Research Lead agent.
        
        Args:
            llm: The language model to use for the agent.
            verbose: Whether to print verbose output.
        """
        super().__init__(
            llm=llm,
            name="AI Research Lead",
            role="Artificial Intelligence Research Lead",
            goal="Research and prototype cutting-edge AI models and techniques that can provide competitive advantage",
            tier=2,  # Specialist Teams
            responsibilities=[
                "Prototype AI models",
                "Align with ethics guidelines",
                "Research emerging AI technologies"
            ],
            meetings=[
                "Model Review Board",
                "Innovation Sprint"
            ],
            verbose=verbose
        )