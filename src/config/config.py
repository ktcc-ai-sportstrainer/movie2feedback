import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')

    CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
    CLAUDE_MODEL = os.getenv('CLAUDE_MODEL', 'claude-')

    LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'openai')  # 'openai' or 'claude'

    INTERACT_PROMPT_PATH = 'data/prompts/interact_prompt.json'
    PLAN_PROMPT_PATH = 'data/prompts/plan_prompt.json'
    SUPPORT_PROMPT_PATH = 'data/prompts/support_prompt.json'