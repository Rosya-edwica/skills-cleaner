from rich.progress import track
import pymorphy2


def set_all_skills_to_infinitive(skills: list[str]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for item in track(range(len(skills)), description="[green]Transform skills to infinitive:"):
        infinitive_skills = bring_all_words_to_the_infinitive(skills[item])
        pairs.append(infinitive_skills)
    return pairs


def bring_all_words_to_the_infinitive(skill: str) -> tuple[str, str]:
    morph = pymorphy2.MorphAnalyzer()
    infinitive = " ".join(morph.parse(i)[0].normal_form for i in skill.split())
    return skill, infinitive
