import asyncio
import websockets

async def hello(websocket, path=None):
    name = await websocket.recv()
    print(f"websocket: < {name}")

    greeting = f"websocket: Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


async def main():
    async with websockets.serve(hello,"localhost", 8765):
        print("websocket: Server contenido en ws://localhost:8765")
        await asyncio.Future() # reemplaza asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("websocket: Servidor cerrado...")