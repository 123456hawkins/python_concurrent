# 多协程
import time
import asyncio


async def message():
    print("hawkins")
    await asyncio.sleep(1)
    print("多线程并发")


def main():
    asyncio.run(message())


if __name__ == "__main__":
    main()
