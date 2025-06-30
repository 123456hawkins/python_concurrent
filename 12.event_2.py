import asyncio

event = asyncio.Event()


async def game():
    print("【%s】起泡准备就绪" % asyncio.current_task().get_name())
    await event.wait()
    print("【%s】百米冲刺的比赛已经开始" % asyncio.current_task().get_name())


async def main():
    tasks = []
    concurrent_limit = 3
    for item in range(1, 7):
        tasks.append(asyncio.create_task(game(), name=f"运动员-{item}"))  # 创建任务
        if item % concurrent_limit == 0:
            await asyncio.sleep(3)
            print("【发号员】运动员已经就绪")
            event.set()  # 设置事件，通知所有等待的任务
            event.clear()  # 清除事件状态，准备下一轮
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
