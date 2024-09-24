import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

    CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
    CLAUDE_MODEL = os.getenv('CLAUDE_MODEL', 'claude-2')

    LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'openai')  # 'openai' or 'claude'

    INTERACT_PROMPT_PATH = 'data/prompts/interact_prompt.json'
    PLAN_PROMPT_PATH = 'data/prompts/plan_prompt.json'
    SUPPORT_PROMPT_PATH = 'data/prompts/support_prompt.json'

    # User configuration
    USER_NAME = os.getenv('USER_NAME', '山田太郎')
    USER_AGE = int(os.getenv('USER_AGE', '13'))
    USER_POSITION = os.getenv('USER_POSITION', '投手')
    USER_EXPERIENCE = int(os.getenv('USER_EXPERIENCE', '2'))
    USER_STRENGTHS = os.getenv('USER_STRENGTHS', '制球力,精神力').split(',')
    USER_WEAKNESSES = os.getenv('USER_WEAKNESSES', 'スタミナ,変化球').split(',')

    @classmethod
    def get_user_data(cls):
        return {
            "name": cls.USER_NAME,
            "age": cls.USER_AGE,
            "position": cls.USER_POSITION,
            "experience": cls.USER_EXPERIENCE,
            "strengths": cls.USER_STRENGTHS,
            "weaknesses": cls.USER_WEAKNESSES
        }