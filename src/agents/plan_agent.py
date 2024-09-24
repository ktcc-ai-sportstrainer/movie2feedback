from typing import Dict
from src.utils.openai_client import OpenAIClient
from src.data.user_data import UserData
from src.utils.logger import logger

class TrainingPlanAgent:
    def __init__(self, openai_client: OpenAIClient, prompt_template: Dict[str, str]):
        self.openai_client = openai_client
        self.prompt_template = prompt_template

    def generate_plan(self, user_data: UserData) -> str:
        logger.info("Generating training plan")
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(user_data)
        
        training_plan = self.openai_client.generate_text(system_prompt, user_prompt)
        
        logger.info("Finished generating training plan")
        return training_plan

    def get_system_prompt(self) -> str:
        return self.prompt_template["system_prompt_temp"]

    def get_user_prompt(self, user_data: UserData) -> str:
        return self.prompt_template["user_prompt_temp"].format(
            name=user_data.name,
            age=user_data.age,
            position=user_data.position,
            experience=user_data.experience,
            strengths=user_data.strengths,
            weaknesses=user_data.weaknesses
        )