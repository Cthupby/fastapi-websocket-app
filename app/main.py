from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocket

app = FastAPI()

html = open('app/templates/index.html', encoding='utf-8').read()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 0
    while True:
        data = await websocket.receive_text()
        i += 1
        await websocket.send_text(f"{i}): {data}")
