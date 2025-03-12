from src.agents.base_agent import BaseAgent
from langchain.schema import BaseLanguageModel

class CMO_CSO(BaseAgent):
    """CMO/CSO agent - Chief Marketing Officer / Chief Sales Officer."""
    
    def __init__(self, llm: BaseLanguageModel, verbose: bool = False):
        """Initialize the CMO/CSO agent.
        
        Args:
            llm: The language model to use for the agent.
            verbose: Whether to print verbose output.
        """
        super().__init__(
            llm=llm,
            name="CMO/CSO",
            role="Chief Marketing Officer / Chief Sales Officer",
            goal="Drive market growth and customer acquisition while ensuring alignment with company vision and values",
            tier=0,  # Leadership Core
            responsibilities=[
                "Align marketing/sales epics with PI goals",
                "Oversee customer retention",
                "Develop go-to-market strategies"
            ],
            meetings=[
                "Iteration Reviews",
                "Market Context Sync"
            ],
            verbose=verbose
        )