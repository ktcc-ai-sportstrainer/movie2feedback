import openai
from typing import List, Dict
from src.utils.logger import logger
from src.utils.llm_client import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model

    def generate_text(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error generating text: {str(e)}")
            return ""

    def generate_conversation(self, messages: List[Dict[str, str]]) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error generating conversation: {str(e)}")
            return ""