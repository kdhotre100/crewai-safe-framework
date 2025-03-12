from src.agents.base_agent import BaseAgent
from langchain.schema import BaseLanguageModel

class Founder(BaseAgent):
    """Founder agent - Strategic decision-maker."""
    
    def __init__(self, llm: BaseLanguageModel, verbose: bool = False):
        """Initialize the Founder agent.
        
        Args:
            llm: The language model to use for the agent.
            verbose: Whether to print verbose output.
        """
        super().__init__(
            llm=llm,
            name="Founder",
            role="Strategic decision-maker",
            goal="Set the overall vision and direction for the company while ensuring alignment with Lean-Agile principles",
            tier=0,  # Leadership Core
            responsibilities=[
                "Finalize strategic themes",
                "Approve PI objectives",
                "Lead I&A workshops"
            ],
            meetings=[
                "PI Planning (Vision Briefing)",
                "Inspect & Adapt"
            ],
            verbose=verbose
        )