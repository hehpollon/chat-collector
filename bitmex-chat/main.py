import asyncio
import websockets

async def recieve(websocket):
    while True:
        data = await websocket.recv()
        print(f"<< {data}")

async def main():
    async with websockets.connect(
            'wss://www.bitmex.com/realtime?subscribe=chat', 
            ssl=True
    ) as websocket:
        fts = [asyncio.ensure_future(recieve(websocket))]
        for f in asyncio.as_completed(fts):
            x = await f
            print(x)

asyncio.get_event_loop().run_until_complete(main())

