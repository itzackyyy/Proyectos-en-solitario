import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    try:

        async with websockets.connect(uri) as websocket:
            name = input("Whats ur name? > ")

            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")
    except ConnectionRefusedError:
        print("Error: No se pudo conectar. ¿Aseguraste que el servidor esté corriendo?")


if __name__ == "__main__":
    # Cambiamos la forma de inicio aquí:
    asyncio.run(hello())