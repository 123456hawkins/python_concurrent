import asyncio

MAX_QUEUE_SIZE = 3
queue = asyncio.Queue(maxsize=MAX_QUEUE_SIZE)
condition = asyncio.Condition()


async def consumer():
    while True:  # 持续消费
        await asyncio.sleep(2)
        async with condition:
            if queue.empty():  # 队列为空
                await condition.wait()
            item = await queue.get()
            print("【%s】%s" % (asyncio.current_task().get_name(), item))
            condition.notify_all()  # 通知所有等待的消费者


async def producer():
    count = 0
    while True:
        # await asyncio.sleep(2)  # 模拟生产时间
        async with condition:
            if queue.full():
                await condition.wait()  # 队列已满，等待消费者消费
            item = f"hawkins商品-第{count + 1}个"
            print("【%s】%s" % (asyncio.current_task().get_name(), item))
            count += 1
            await queue.put(item)
            condition.notify_all()  # 通知所有等待的消费者


async def main():
    tasks = [
        asyncio.create_task(consumer(), name="消费者"),
        asyncio.create_task(producer(), name="生产者"),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
