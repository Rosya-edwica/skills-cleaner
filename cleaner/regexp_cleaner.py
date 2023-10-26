import tools
from config import STOP_SKILLS_CSV_FILENAME
import re
from models import Skill

STOP_SYMBOLS = {
        "_",
        "*",
        "?",
        "•",
        "#",
        "–",
        "«",
        "»",
        "'",
        '"'
    }

REMOVE_SYMBOLS = {
        ",",
        ";",
        "/",
        "\\",
        "|"
    }

def find_stop_skills(skills: list[Skill]) -> list[Skill]:
    """Возвращает стоп-навыки"""
    
    skills_count = len(skills)
    stop_skills_set = set((i.lower().strip() for i in  tools.load_skills(STOP_SKILLS_CSV_FILENAME)))


    finded_stop_skills = [skill for skill in skills if skill.Name.lower().strip() in stop_skills_set]
    print("Найдено стоп-навыков:", len(finded_stop_skills))
    # print(f"Количество навыков после удаления стоп-навыков: {len(skills_without_stop)} (-{tools.calculate_the_difference_in_percentages(skills_count, len(skills_without_stop))}%)")
    return finded_stop_skills


def cut_stop_symbols(skills: list[Skill]) -> list[Skill]:
    counter = 0
    
    updated_skills = []
    for item in skills:
        
        new_name = re.sub(r"\*|\?|•|#|«|»|'|\"|", "", item.Name)
        new_name = re.sub(r"_|-", " ", new_name)
        item.NewName = new_name
        if item.Name != item.NewName:
            updated_skills.append(item)
            counter += 1
    print(f"Количество навыков, содержащих стоп-символы: {counter} (-{tools.calculate_the_difference_in_percentages(len(skills), counter)}%)")
    return updated_skills


def find_skills_with_stop_symbols(skills: list[Skill]) -> list[Skill]:
    counter = 0
    
    finded = []
    for item in skills:
        has_remove_symbols = re.findall(r",|;|\\", item.Name)
        if has_remove_symbols:
            finded.append(item)
            counter += 1
    print(f"Количество навыков, содержащих стоп-символы, подлежающих удалению: {counter} (-{tools.calculate_the_difference_in_percentages(len(skills), counter)}%)")
    return finded



def clean_skills(skills: list[Skill]) -> list[Skill]:
    updated = []
    for skill in skills:
        skill.Name = re.sub("опыт работы со |опыт работы с |знание |умение |работа в |работать в |готовность| желание| программирование на |навыки |базовые |база |опыт ", "", skill.Name.lower())
        updated.append(skill)
    print("Обработали навыки")
    return updated