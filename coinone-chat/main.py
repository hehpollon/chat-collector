import asyncio
import websockets

async def ping(websocket):
    while True:
        await asyncio.sleep(25)
        print(f">> {2}")
        await websocket.send("2")

async def recieve(websocket):
    while True:
        data = await websocket.recv()
        print(f"<< {data}")

async def main():
    async with websockets.connect(
            'wss://chat.coinone.co.kr/socket.io/?EIO=3&transport=websocket',
            ssl=True
    ) as websocket:
        data = await websocket.recv()
        print(f"< {data}")

        await websocket.send("40/chat,")
        data = await websocket.recv()
        print(f"< {data}")

        fts = [asyncio.ensure_future(ping(websocket)), asyncio.ensure_future(recieve(websocket))]
        for f in asyncio.as_completed(fts):
            x = await f
            print(x)

asyncio.get_event_loop().run_until_complete(main())

