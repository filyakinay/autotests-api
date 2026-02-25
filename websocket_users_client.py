import asyncio
import websockets


async def start_client():
    uri = "ws://localhost:8765"

    # Устанавливаем соединение с сервером
    async with websockets.connect(uri) as websocket:
        # Отправляем приветственное сообщение
        print("Отправка сообщения серверу: Привет, сервер!")
        await websocket.send("Привет, сервер!")

        # Получаем и выводим 5 ответных сообщений
        print("Ожидание 5 сообщений от сервера...")
        for _ in range(5):
            message = await websocket.recv()
            print(f"Получено от сервера: {message}")


if __name__ == "__main__":
    try:
        asyncio.run(start_client())
    except Exception as e:
        print(f"Ошибка: {e}")