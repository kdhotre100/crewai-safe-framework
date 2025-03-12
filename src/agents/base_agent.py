from crewai import Agent
from langchain.schema import BaseLanguageModel

class BaseAgent:
    """Base class for all agents in the system."""
    
    def __init__(
        self,
        llm: BaseLanguageModel,
        name: str = None,
        role: str = None,
        goal: str = None,
        tier: int = None,
        backstory: str = None,
        responsibilities: list = None,
        meetings: list = None,
        verbose: bool = False
    ):
        """Initialize a new agent.
        
        Args:
            llm: The language model to use for the agent.
            name: The name of the agent.
            role: The role of the agent.
            goal: The goal of the agent.
            tier: The tier of the agent (0, 1, or 2).
            backstory: The backstory of the agent.
            responsibilities: The responsibilities of the agent.
            meetings: The meetings the agent attends.
            verbose: Whether to print verbose output.
        """
        self.llm = llm
        self.name = name or self.__class__.__name__
        self.role = role or "Agent"
        self.goal = goal or "Accomplish tasks efficiently"
        self.tier = tier if tier is not None else 2  # Default to tier 2
        self.responsibilities = responsibilities or []
        self.meetings = meetings or []
        self.verbose = verbose
        self._backstory = backstory
    
    def _generate_backstory(self):
        """Generate a backstory for the agent based on its role, responsibilities, and meetings."""
        backstory = f"{self.name} is a {self.role} in the organization.\n\n"
        
        if self.responsibilities:
            backstory += "Responsibilities:\n"
            for resp in self.responsibilities:
                backstory += f"- {resp}\n"
            backstory += "\n"
        
        if self.meetings:
            backstory += "Regularly attends these meetings:\n"
            for meeting in self.meetings:
                backstory += f"- {meeting}\n"
            backstory += "\n"
        
        return backstory
    
    def to_agent(self):
        """Convert this agent to a CrewAI Agent."""
        if not self._backstory:
            self._backstory = self._generate_backstory()
        
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self._backstory,
            verbose=self.verbose,
            llm=self.llm,
            allow_delegation=True
        )