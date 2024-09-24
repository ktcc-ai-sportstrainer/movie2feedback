from dataclasses import dataclass
from typing import List

@dataclass
class UserData:
    name: str
    age: int
    position: str
    experience: int
    strengths: List[str]
    weaknesses: List[str]