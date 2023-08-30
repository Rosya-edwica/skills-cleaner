import sys

import cleaner
import db

ERROR_MESSAGE = "\n\t".join([
        "Запустите программу с дополнительным аргументом:",
        "1. translate - для перевода навыков на английский язык",
        "2. update - для очистки названий навыков от лишних символов",
        "3. remove - пометить ненужные навыки, как удаленные в БД",
    ])

def translate():
    print("Запущен перевод навыков на английский язык")
    while True:
        skills = db.get_skills_for_translation()
        if not skills: 
            break
        db.translate_skills(skills)
        break


def remove_stop_skills():
    print("Запущена очистка навыков от мусора")
    
    skills = db.get_all_skills()
    skills_to_remove = cleaner.find_skills_with_stop_symbols(skills)
    if skills_to_remove:
        db.mark_skills_like_deleted(skills_to_remove)
    
    skills_to_remove = cleaner.find_stop_skills(skills)
    if skills_to_remove:
        db.mark_skills_like_deleted(skills_to_remove)
    

def update():
    print("Запущена очистка названий навыков")
    skills = db.get_all_skills()
    updated_skills = cleaner.cut_stop_symbols(skills)
    if updated_skills:
        db.update_skills(updated_skills)


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        exit(ERROR_MESSAGE)
        
    match args[0]:
        case "translate": translate()
        case "update": update()
        case "remove": remove_stop_skills()
        case _: exit(ERROR_MESSAGE)
    



if __name__ == "__main__":
    main()
