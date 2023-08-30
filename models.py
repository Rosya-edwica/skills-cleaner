from dataclasses import dataclass


@dataclass(slots=True)
class Skill:
    Id: int
    Name: str
    NewName: str