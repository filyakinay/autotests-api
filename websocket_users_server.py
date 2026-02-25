import asyncio
import websockets


# Функция для обработки подключений
async def handle_user_connection(websocket):
    print("Новый пользователь подключился")
    try:
        async for message in websocket:
            print(f"Получено сообщение от пользователя: {message}")

            # Цикл отправки 5 сообщений, которые ждет клиент
            for i in range(1, 6):
                await websocket.send(f"Ответ сервера №{i} на ваше сообщение")

    except websockets.exceptions.ConnectionClosedOK:
        print("Пользователь отключился")


# Запуск сервера
async def main():
    # Сервер будет слушать на localhost, порт 8765
    async with websockets.serve(handle_user_connection, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        await asyncio.Future()  # запуск бесконечного ожидания


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nСервер остановлен")