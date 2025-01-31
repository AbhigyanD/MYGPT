import asyncio
import openai
import websockets
import json

# OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key"

# Function to connect to the Realtime API
async def connect_realtime_api():
    uri = "wss://api.openai.com/v1/realtime"  # WebSocket endpoint

    async with websockets.connect(uri) as websocket:
        # Send authentication request
        await websocket.send(json.dumps({"auth": {"api_key": OPENAI_API_KEY}}))

        # Example: Request real-time opinion on asset price
        request = {
            "session": {"modalities": ["text"]},
            "conversation": {
                "item": {
                    "type": "message",
                    "role": "user",
                    "content": [{"type": "input_text", "text": "Is Tesla stock overvalued?"}]
                }
            }
        }

        # Send request
        await websocket.send(json.dumps(request))

        # Receive and process response
        while True:
            response = await websocket.recv()
            response_data = json.loads(response)
            if response_data.get("type") == "response.text.done":
                break  # Stop when the response is complete

            if response_data.get("type") == "response.text.delta":
                print(response_data["delta"], flush=True, end="")

# Run WebSocket connection
asyncio.run(connect_realtime_api())
