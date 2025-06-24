# 协程存在的问题
import asyncio

ticket = 5


async def sale():
    global ticket
    while True > 0:
        if ticket > 0:
            await asyncio.sleep(1)  # 模拟处理时间
            ticket -= 1

            print(
                "【%s】售出一张票，剩余票数%s"
                % (asyncio.current_task().get_name(), ticket)
            )
        else:
            # 票已售空
            print("【%s】票已售空" % (asyncio.current_task().get_name()))
            break


async def main():
    tasks = [
        asyncio.create_task(sale(), name=f"售票员==={item}===") for item in range(3)
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
