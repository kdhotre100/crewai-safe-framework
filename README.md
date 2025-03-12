# CrewAI SAFe 6.0 Framework Implementation

This project implements a multi-agent system using CrewAI, structured according to the Scaled Agile Framework (SAFe) 6.0. It demonstrates how AI agents can collaborate in an organizational structure to accomplish complex tasks.

## Project Structure

```
.
├── .env                  # Environment variables (API keys)
├── requirements.txt      # Project dependencies
├── src/
│   ├── main.py           # Main script for running the full crew
│   ├── demo_agent.py     # Simple demo of a single agent interaction
│   ├── multi_agent_demo.py # Demo of multiple agents collaborating
│   ├── test_agents.py    # Script to test agent initialization
│   └── agents/
│       ├── __init__.py   # Package initialization
│       └── individual/   # Individual agent implementations
│           ├── __init__.py  # Exports all agents
│           ├── founder.py   # Founder agent implementation
│           ├── ceo.py       # CEO agent implementation
│           └── ...          # Other agent implementations
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your environment variables in `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Running the Simple Demo

To run a simple interaction with the Founder agent:

```
python -m src.demo_agent
```

### Running the Multi-Agent Demo

To run a demonstration of multiple agents (Founder, CEO, CTO/CAI) collaborating:

```
python -m src.multi_agent_demo
```

### Testing Agent Initialization

To verify that all agents can be initialized correctly:

```
python -m src.test_agents
```

### Running the Full Crew

To run the full crew with all agents:

```
python -m src.main
```

## Agent Structure

The agents are organized according to the SAFe 6.0 framework, with different tiers:

- **Tier 0**: Executive leadership (Founder, CEO, CTO/CAI)
- **Tier 1**: Middle management and department heads
- **Tier 2**: Specialists and team members

Each agent has:
- A specific role
- A defined goal
- A set of responsibilities
- Meetings they attend

## Customization

You can modify the agents' behaviors by editing their respective files in the `src/agents/individual/` directory. Each agent class inherits from the base `Agent` class and can be customized with different goals, responsibilities, and backstories.

## Model Configuration

The project is configured to use the `o3-mini` model from OpenAI. You can change the model by modifying the `model` parameter in the `ChatOpenAI` initialization in the respective script files.