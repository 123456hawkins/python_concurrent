import asyncio


async def echo_handler(reader, writer):
    while True:

        data = await reader.read(100)  # 从客户端接收数据
        message = data.decode()  # 解码数据
        if message.lower() == "exit":
            writer.close()  # 关闭连接
        # 每一个输出通道之中都会保存客户端的访问地址信息
        client_address = writer.get_extra_info("peername")  # 客户端地址
        print(f'【ECHO服务端】接收来自"{client_address}"的数据：{message}')
        echo_message = f"Echo: {message}"
        writer.write(echo_message.encode())  # 将数据发送回客户端
        await writer.drain()  # 强制性刷新输出缓冲区


async def main():
    server = await asyncio.start_server(echo_handler, "127.0.0.1", 8888)
    server_address = server.sockets[0].getsockname()
    print(f"【ECHO服务端】正在运行，监听地址：{server_address}")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
