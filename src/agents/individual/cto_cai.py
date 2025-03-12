from src.agents.base_agent import BaseAgent
from langchain.schema import BaseLanguageModel

class CTO_CAI(BaseAgent):
    """CTO/CAI agent - Chief Technology Officer / Chief AI Officer."""
    
    def __init__(self, llm: BaseLanguageModel, verbose: bool = False):
        """Initialize the CTO/CAI agent.
        
        Args:
            llm: The language model to use for the agent.
            verbose: Whether to print verbose output.
        """
        super().__init__(
            llm=llm,
            name="CTO/CAI",
            role="Chief Technology Officer / Chief AI Officer",
            goal="Lead technological innovation and AI strategy while ensuring ethical implementation and technical excellence",
            tier=0,  # Leadership Core
            responsibilities=[
                "Maintain technical runway",
                "Enforce AI ethics",
                "Oversee DevOps/CD pipelines"
            ],
            meetings=[
                "System Demos",
                "Architectural Sync"
            ],
            verbose=verbose
        )