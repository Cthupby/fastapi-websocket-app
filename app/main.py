from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocket

from . import models
from .database import session

app = FastAPI()

# шаблон для отображения постов
html = open('app/templates/index.html', encoding='utf-8').read()


# функция добавления постов в бд
async def add_post(post_number, post):
    post = models.Post(post_number=post_number,
                       post=post)
    session.add(post)
    session.commit()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # получение данных из бд
    all_posts = session.query(models.Post).all()
    for post in all_posts:
        # отправление данных из бд в шаблон
        await websocket.send_text(f"{post.post_number} : {post.post}")
    number = 0
    while True:
        # получение новых данных
        post = await websocket.receive_text()
        number += 1
        await websocket.send_text(f"{number} : {post}")
        # добавление новых данных в бд
        await add_post(number, post)
