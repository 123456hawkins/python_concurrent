import asyncio


async def main():

    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)
    while True:
        message = input("输入要发送的信息")
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(100)
        print(f"接收到服务器的回应：{data.decode()}")
        if message.lower() == "exit":
            print("客户端关闭连接")
            break
    print("关闭网络连接，本次交互结束")
    writer.close()


if __name__ == "__main__":
    asyncio.run(main())
