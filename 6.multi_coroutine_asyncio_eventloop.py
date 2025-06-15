# 多协程

import asyncio


async def message():
    print("hawkins")
    await asyncio.sleep(1)
    return "hawkins多线程并发"


def main():
    try:
        event_loop = asyncio.get_event_loop()
        result = event_loop.run_until_complete(message())
        print("【业务处理结果】%s" % result)
    finally:
        event_loop.close()


if __name__ == "__main__":
    main()
