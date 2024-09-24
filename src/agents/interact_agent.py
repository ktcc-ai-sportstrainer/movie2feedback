from typing import Dict
from src.utils.openai_client import OpenAIClient
from src.data.user_data import UserData
from src.utils.logger import logger

class ConversationAgent:
    def __init__(self, openai_client: OpenAIClient, prompt_template: Dict[str, str]):
        self.openai_client = openai_client
        self.prompt_template = prompt_template

    def interact(self, user_data: UserData) -> UserData:
        logger.info("Starting conversation with user")
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(user_data)
        
        conversation = self.openai_client.generate_text(system_prompt, user_prompt)
        updated_user_data = self.extract_user_data(conversation, user_data)
        
        logger.info("Finished conversation with user")
        return updated_user_data

    def get_system_prompt(self) -> str:
        return self.prompt_template["system_prompt_temp"]

    def get_user_prompt(self, user_data: UserData) -> str:
        return self.prompt_template["user_prompt_temp"].format(
            name=user_data.name,
            age=user_data.age,
            position=user_data.position,
            experience=user_data.experience
        )

    def extract_user_data(self, conversation: str, user_data: UserData) -> UserData:
        # Implement logic to extract updated user data from the conversation
        # This is a placeholder and should be replaced with actual implementation
        return user_data