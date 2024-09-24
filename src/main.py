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
    conversation_prompt = load_prompt(Config.CONVERSATION_PROMPT_PATH)
    training_plan_prompt = load_prompt(Config.TRAINING_PLAN_PROMPT_PATH)
    motivational_prompt = load_prompt(Config.MOTIVATIONAL_PROMPT_PATH)

    # Create LLM client
    llm_client = get_llm_client()

    # Create agents
    conversation_agent = ConversationAgent(llm_client, conversation_prompt)
    training_plan_agent = TrainingPlanAgent(llm_client, training_plan_prompt)
    motivational_agent = MotivationalAgent(llm_client, motivational_prompt)

    # Initial user data (this could be loaded from a file or database)
    user_data = UserData(name="", age=0, position="", experience=0, strengths=[], weaknesses=[])

    # Conversation phase
    user_data = conversation_agent.interact(user_data)

    # Training plan generation
    training_plan = training_plan_agent.generate_plan(user_data)

    # Motivational message generation
    motivation = motivational_agent.generate_motivation(user_data, training_plan)

    # Output results
    print("Training Plan:")
    print(training_plan)
    print("\nMotivational Message:")
    print(motivation)

    logger.info("AI Sports Trainer session completed")

if __name__ == "__main__":
    main()