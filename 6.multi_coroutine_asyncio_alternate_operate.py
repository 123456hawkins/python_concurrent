# 多协程

import asyncio


async def coroutine_task(author, book):
    for item in range(5):
        print(
            "【%s】图书作者：%s, 图书名称：%s"
            % (asyncio.current_task().get_name(), author, book)
        )
        await asyncio.sleep(1)


async def coroutine_start():
    tasks = [
        asyncio.create_task(
            coroutine_task("hawkins", "python并发编程"), name="hawkins-task-python"
        ),
        asyncio.create_task(
            coroutine_task("hawkins", "java并发编程"), name="hawkins-task-java"
        ),
        asyncio.create_task(
            coroutine_task("hawkins", "go并发编程"), name="hawkins-task-go"
        ),
        asyncio.create_task(
            coroutine_task("hawkins", "mysql并发编程"), name="hawkins-task-mysql"
        ),
    ]
    await asyncio.gather(*tasks)


def main():
    asyncio.run(coroutine_start())


if __name__ == "__main__":
    main()
