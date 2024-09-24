import anthropic
from typing import List, Dict
from src.utils.logger import logger
from src.utils.llm_client import LLMClient

class ClaudeClient(LLMClient):
    def __init__(self, api_key: str, model: str = "claude-2"):
        self.client = anthropic.Client(api_key)
        self.model = model

    def generate_text(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self.client.completion(
                model=self.model,
                prompt=f"{anthropic.HUMAN_PROMPT} {system_prompt}\n\n{user_prompt}{anthropic.AI_PROMPT}",
                max_tokens_to_sample=1000,
            )
            return response.completion
        except Exception as e:
            logger.error(f"Error generating text: {str(e)}")
            return ""

    def generate_conversation(self, messages: List[Dict[str, str]]) -> str:
        try:
            conversation = ""
            for message in messages:
                if message["role"] == "system":
                    conversation += f"{anthropic.HUMAN_PROMPT} {message['content']}\n"
                elif message["role"] == "user":
                    conversation += f"{anthropic.HUMAN_PROMPT} {message['content']}\n"
                elif message["role"] == "assistant":
                    conversation += f"{anthropic.AI_PROMPT} {message['content']}\n"
            
            response = self.client.completion(
                model=self.model,
                prompt=f"{conversation}{anthropic.AI_PROMPT}",
                max_tokens_to_sample=1000,
            )
            return response.completion
        except Exception as e:
            logger.error(f"Error generating conversation: {str(e)}")
            return ""