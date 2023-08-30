import csv
from config import OUTPUT_CSV_FILENAME

def load_skills(path: str) -> list[str]:
    skills: list[str] = []
    with open(path, mode="r", encoding="utf-8", newline="") as file:
        csv_file = csv.reader(file, delimiter=",")
        for row in csv_file:
            if row[0] == "": continue
            skills.append(row[0])
    return skills


def save_skills(skills: list[str]) -> None:
    with open(OUTPUT_CSV_FILENAME   , mode="w", encoding="utf-8", newline="") as file:
        csv_file = csv.writer(file)
        csv_file.writerows((i, ) for i in skills)




def calculate_the_difference_in_percentages(reduced: int|float, deductible: int|float) -> int|float:
    if reduced == 0: raise ZeroDivisionError
    return round((reduced-deductible)/reduced * 100, 2)
