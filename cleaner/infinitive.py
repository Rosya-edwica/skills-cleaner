from rich.progress import track
from models import Skill
import pymorphy3



def modify_skills_to_infinivive(skills: list[Skill]) -> list[Skill]:
    updated = []
    for item in track(range(len(skills)), description="[green]Transform skills to infinitive:"):
        skill = skills[item]
        infinitive_form = bring_all_words_to_the_infinitive(skill.Name)
        updated.append(Skill(
            Id=skill.Id,
            Name=skill.Name,
            NewName=infinitive_form
        ))
    return updated


def bring_all_words_to_the_infinitive(skill: str) -> str:
    morph = pymorphy3.MorphAnalyzer()
    infinitive = " ".join(morph.parse(i)[0].normal_form for i in skill.split())
    return infinitive
