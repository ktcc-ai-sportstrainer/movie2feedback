from typing import Dict
from src.utils.llm_client import LLMClient
from src.persona.user_data import UserData
from src.utils.logger import logger

class SupportAgent:
    def __init__(self, llm_client: LLMClient, prompt_template: Dict[str, str]):
        self.llm_client = llm_client
        self.prompt_template = prompt_template

    def generate_support(self, user_data: UserData, training_plan: str) -> str:
        logger.info("Generating support message")
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(user_data, training_plan)
        
        support_message = self.llm_client.generate_text(system_prompt, user_prompt)
        
        logger.info("Finished generating support message")
        return support_message

    def get_system_prompt(self) -> str:
        return self.prompt_template["system_prompt_temp"]

    def get_user_prompt(self, user_data: UserData, training_plan: str) -> str:
        return self.prompt_template["user_prompt_temp"].format(
            name=user_data.name,
            age=user_data.age,
            position=user_data.position,
            training_plan=training_plan
        )