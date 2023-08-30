from db import connect
from models import Skill
from rich.progress import track
from googletrans import Translator


def get_skills_for_translation() -> list[Skill]:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, name FROM demand WHERE is_custom IS NULL AND is_deleted is false and translated IS NULL LIMIT 500")
    skills = [Skill(*row) for row in cursor.fetchall()]
    conn.close()
    return skills

def get_all_skills() -> list[Skill]:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, name FROM demand WHERE is_custom IS NULL AND is_deleted is false")
    skills = [Skill(*row) for row in cursor.fetchall()]
    conn.close()
    return skills


def update_skills(skills: list[Skill]) -> None:
    conn = connect()
    cursor = conn.cursor()
    for i in track(range(len(skills)), description="Обновляем навыки"):
        query = f"UPDATE demand SET name='{skills[i].NewName}' WHERE id = {skills[i].Id}"
        cursor.execute(query)
    conn.commit()
    conn.close()
    
    
def mark_skills_like_deleted(skills: list[Skill]) -> None:
    conn = connect()
    cursor = conn.cursor()
    for i in track(range(len(skills)), description="Отмечаем навыки, как удаленные"):
        query = f"UPDATE demand SET is_deleted=true WHERE id = {skills[i].Id}"
        cursor.execute(query)
    conn.commit()
    conn.close()
    

def translate_skills(skills: list[Skill]):
    conn = connect()
    cursor = conn.cursor()
    trans = Translator()
    for i in track(range(len(skills)), description="Обновляем навыки"):
        translated =  trans.translate(text=skills[i].Name, dest="en", src="ru").text
        query = f"UPDATE demand SET translated='{translated}' WHERE id = {skills[i].Id}"
        cursor.execute(query)
        conn.commit()
    conn.close()