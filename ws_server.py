import asyncio
import re
import websockets
import numpy as np


async def audio_server(websocket, path):
  # Extract sample rate from path using regex
  match = re.match(r"/(\d+)", path)
  if match:
    client_sample_rate = int(match.group(1))
    print(f"Received client sample rate from path: {client_sample_rate} Hz")
  else:
    print("Invalid path. Sample rate not provided.")
    await websocket.close()
    return

  async for message in websocket:
    # Convert received buffer to numpy array
    audio_data = np.frombuffer(message, dtype=np.float32)

    # Just echo

    # Convert to float32 byte data and send directly
    audio_data_bytes = audio_data.astype(np.float32).tobytes()
    await websocket.send(audio_data_bytes)


# Start WebSocket server
start_server = websockets.serve(audio_server, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
