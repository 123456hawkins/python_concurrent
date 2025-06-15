# 多协程

import asyncio


async def coroutine_task(author, book):
    await asyncio.sleep(2)
    return f"作者: {author}, 书名: {book}"


async def coroutine_start():
    task_python = asyncio.create_task(
        coroutine_task("hawkins", "python并发编程"), name="hawkins-task-python"
    )
    task_java = asyncio.create_task(
        coroutine_task("hawkins", "java并发编程"), name="hawkins-task-java"
    )
    print(await task_python)
    print(await task_java)


def main():
    asyncio.run(coroutine_start())


if __name__ == "__main__":
    main()
