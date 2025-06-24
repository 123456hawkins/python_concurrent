# 异步上下文管理
import asyncio


class Message:
    class Connect:
        def build(self):
            print("【网络管理】建立连接")

        def close(self):
            print("【网络管理】关闭连接")

    def __init__(self) -> None:
        self.__result = "Nothing"
        self.__connect = Message.Connect()

    async def __aenter__(self):
        self.__connect.build()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"【消息处理】传入的值: {self.__result}")
        self.__connect.close()
        if exc_type:
            print(f"【异常处理】异常类型: {exc_type}, 异常值: {exc_val}")
        else:
            print("【网络管理】关闭网络连接")
            return True

    async def message_handler(self, task):
        while not task.done():
            print("【消息处理】正在处理消息")
            await asyncio.sleep(1)
        else:
            self.__result = task.result()
            print("【消息处理】消息处理完成")


async def message_echo(message):
    await asyncio.sleep(2)
    return f"Echo: {message}"


async def main():
    async with Message() as msg:
        task = asyncio.create_task(message_echo("hawkins"))
        await msg.message_handler(task)


if __name__ == "__main__":
    asyncio.run(main())
