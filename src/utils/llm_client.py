from abc import ABC, abstractmethod
from typing import List, Dict

class LLMClient(ABC):
    @abstractmethod
    def generate_text(self, system_prompt: str, user_prompt: str) -> str:
        pass

    @abstractmethod
    def generate_conversation(self, messages: List[Dict[str, str]]) -> str:
        pass