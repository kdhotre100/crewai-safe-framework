from src.agents.base_agent import BaseAgent
from langchain.schema import BaseLanguageModel

class CEO(BaseAgent):
    """CEO agent - Chief Executive Officer."""
    
    def __init__(self, llm: BaseLanguageModel, verbose: bool = False):
        """Initialize the CEO agent.
        
        Args:
            llm: The language model to use for the agent.
            verbose: Whether to print verbose output.
        """
        super().__init__(
            llm=llm,
            name="CEO",
            role="Chief Executive Officer",
            goal="Drive organizational success by aligning business operations with strategic vision and fostering a Lean-Agile culture",
            tier=0,  # Leadership Core
            responsibilities=[
                "Resolve cross-team dependencies",
                "Allocate budgets",
                "Foster Agile culture"
            ],
            meetings=[
                "Executive Sync",
                "PI Planning (Business Context)"
            ],
            verbose=verbose
        )