from fastapi import APIRouter
import logging as log
from starlette.websockets import WebSocket, WebSocketDisconnect

log.basicConfig(level=log.INFO)
ws_router = APIRouter()


@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        # There is already a log message when the socket is closed
        pass
