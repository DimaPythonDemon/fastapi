from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import logging
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory='templates/html')


def load_achievements_from_file(file_path):
    achievements = {}
    with open(file_path, 'r') as file:
        for line in file:
            try:
                name, description = line.strip().split(':')
                achievements[name.strip()] = description.strip()
            except:
                logging.error("Error loading achievements from file")
    return achievements



achievements_data = load_achievements_from_file('achievements.txt')
achievements_json = json.dumps(achievements_data, ensure_ascii=False, indent=4)


@app.get('/new_achievement', response_class=HTMLResponse)
async def show_achievements_form(request: Request):
    return templates.TemplateResponse('achievements_form.html', {'request': request})


@app.get('/achievements', response_class=HTMLResponse)
async def show_achievements(request: Request):
    achievements_data = load_achievements_from_file('achievements.txt')
    return templates.TemplateResponse('achievements.html', {'request': request, 'achievements': achievements_data})


def save_achievement_to_file(achievement_name, achievement_description):
    with open('achievements.txt', 'a') as file:
        file.write(f"{achievement_name}: {achievement_description}\n")


@app.post('/add_achievement')
async def add_achievement(
        achievement_name: str = Form(...),
        achievement_description: str = Form(...)):
    save_achievement_to_file(achievement_name, achievement_description)

    return {'message': f'Достижение "{achievement_name}" успешно добавлено!'}