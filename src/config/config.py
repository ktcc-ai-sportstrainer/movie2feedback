import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

    CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
    CLAUDE_MODEL = os.getenv('CLAUDE_MODEL', 'claude-2')

    LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'openai')  # 'openai' or 'claude'

    CONVERSATION_PROMPT_PATH = 'data/prompts/conversation_prompt.json'
    TRAINING_PLAN_PROMPT_PATH = 'data/prompts/training_plan_prompt.json'
    MOTIVATIONAL_PROMPT_PATH = 'data/prompts/motivational_prompt.json'