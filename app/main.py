from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/html')


@app.get('/achievements', response_class=HTMLResponse)
async def show_achievements_form(request: Request):
    return templates.TemplateResponse('achievements_form.html', {'request': request})


# Обработка данных из формы
@app.post('/add_achievement')
async def add_achievement(
        achievement_name: str = Form(...),
        achievement_description: str = Form(...)
):
    # Здесь можно добавить логику для сохранения достижения в базе данных или другие действия
    # Например:
    # save_achievement_to_database(achievement_name, achievement_description)

    return {'message': f'Достижение "{achievement_name}" успешно добавлено!'}

# Пример HTML-шаблона (achievements_form.html)
# <form method="post" action="/add_achievement">
#     <input type="text" name="achievement_name" placeholder="Название достижения">
#     <input type="text" name="achievement_description" placeholder="Описание достижения">
#     <button type="submit">Добавить</button>
# </form>
