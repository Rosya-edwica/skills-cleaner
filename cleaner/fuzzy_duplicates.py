from fuzzywuzzy import process


def match_skills_by_fuzzy(skills: list[str]) -> list[str]:
    for index, item in enumerate(skills):
        if item == "": continue
        pair = process.extractOne(item, skills[index+1:])
        if pair[0]:
            print(f"Пара для навыка: {item} = {pair}")
        else:
            print(f"Нет пары для: {item}")