# FastAPI Server Setup
from fastapi import FastAPI, WebSocket
import asyncio
from services.realtime_api import connect_realtime_api
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

app = FastAPI()

@app.websocket("/realtime")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await connect_realtime_api()  # Connect to OpenAI Realtime API
    await websocket.close()
