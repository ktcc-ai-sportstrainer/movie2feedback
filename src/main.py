from src.agents.interact_agent import InteractAgent
from src.agents.plan_agent import PlanAgent
from src.agents.support_agent import SupportAgent
from src.persona.user_data import UserData
from src.utils.openai_client import OpenAIClient
from src.utils.claude_client import ClaudeClient
from src.utils.logger import logger
from src.config.config import Config
import json

def load_prompt(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def get_llm_client():
    if Config.LLM_PROVIDER == 'openai':
        if not Config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
        return OpenAIClient(Config.OPENAI_API_KEY, Config.OPENAI_MODEL)
    elif Config.LLM_PROVIDER == 'claude':
        if not Config.CLAUDE_API_KEY:
            raise ValueError("Claude API key not found. Please set CLAUDE_API_KEY in your .env file.")
        return ClaudeClient(Config.CLAUDE_API_KEY, Config.CLAUDE_MODEL)
    else:
        raise ValueError(f"Invalid LLM provider: {Config.LLM_PROVIDER}")

def main():
    logger.info("Starting AI Sports Trainer")

    # Load prompts
    interact_prompt = load_prompt(Config.INTERACT_PROMPT_PATH)
    plan_prompt = load_prompt(Config.PLAN_PROMPT_PATH)
    support_prompt = load_prompt(Config.SUPPORT_PROMPT_PATH)

    # Create LLM client
    llm_client = get_llm_client()

    # Create agents
    interact_agent = InteractAgent(llm_client, interact_prompt)
    plan_agent = PlanAgent(llm_client, plan_prompt)
    support_agent = SupportAgent(llm_client, support_prompt)

    # Load user data from config
    user_data = UserData(**Config.get_user_data())

    # Interaction phase
    user_data = interact_agent.interact(user_data)

    # Training plan generation
    training_plan = plan_agent.generate_plan(user_data)

    # Support message generation
    support_message = support_agent.generate_support(user_data, training_plan)

    # Output results
    print("User Data:")
    print(user_data)
    print("\nTraining Plan:")
    print(training_plan)
    print("\nSupport Message:")
    print(support_message)

    logger.info("AI Sports Trainer session completed")

if __name__ == "__main__":
    main()