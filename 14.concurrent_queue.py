import asyncio

MAX_QUEUE_SIZE = 3
queue = asyncio.Queue(maxsize=MAX_QUEUE_SIZE)


async def consumer():
    while True:  # 持续消费
        await asyncio.sleep(2)
        item = await queue.get()
        print("【%s】%s" % (asyncio.current_task().get_name(), item))


async def producer():
    count = 0
    while True:
        asyncio.sleep(0.01)
        item = f"hawkins商品-第{count + 1}个"
        print("【%s】%s" % (asyncio.current_task().get_name(), item))
        count += 1
        await queue.put(item)


async def main():
    tasks = [
        asyncio.create_task(consumer(), name="消费者"),
        asyncio.create_task(producer(), name="生产者"),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
