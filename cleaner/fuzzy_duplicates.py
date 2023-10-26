from fuzzywuzzy import process
from models import Skill
from time import perf_counter
from rich.progress import track


def match_skills_by_fuzzy(skills: list[Skill]) -> list[str]:
    for index in track(range(len(skills)), description="Duplicate searching..."):
        skill = skills[index]
        duplicates  = []
        pair = process.extract(skill.Name, skills[index+1:], limit=3)
        for i in pair:
            duplicates.append(f"{skill.Id}|{skill.Name}:{i[0].Id}:{i[0].Name}:{i[-1]}")
        add_to_logs(duplicates)
            
def add_to_logs(data: list[str]):
    if not data: return
    file = open("fuzzy_logs.txt", mode="a", encoding="utf-8")
    file.write("\n".join(data))
    file.close()


def match_skills_by_infinitive(skills: list[Skill]) -> dict[int, list[int]]:
    cash = {}
    s = perf_counter()
    print("Длина", len(skills))

    for index in track(range(len(skills)), description="Duplicate searching..."):
        skill_one = skills[index]
        for _, skill_two in enumerate(skills[index+1:]):
            skill_one_set = set(skill_one.Name.split())
            skill_two_set = set(skill_two.Name.split())

            if skill_one_set == skill_two_set:
                if skill_one.Id in cash:
                    cash[skill_one.Id].append(skill_two.Id)
                else:
                    cash[skill_one.Id] = [skill_two.Id, ]
    print(perf_counter() - s, "seconds.")
    return cash
