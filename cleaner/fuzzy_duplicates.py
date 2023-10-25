from fuzzywuzzy import process
from models import Skill
from time import perf_counter
from rich.progress import track


def match_skills_by_fuzzy(skills: list[str]) -> list[str]:
    for index, item in enumerate(skills):
        if item == "": continue
        pair = process.extractOne(item, skills[index+1:])
        if pair[0]:
            print(f"Пара для навыка: {item} = {pair}")
        else:
            print(f"Нет пары для: {item}")



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
