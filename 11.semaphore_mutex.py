# semaphore信号量

import asyncio

semaphore = asyncio.Semaphore(3)


async def bank():

    while True:
        async with semaphore:
            print(f"【{asyncio.current_task().get_name()}】正在办理业务")
            await asyncio.sleep(2)
            print(f"【{asyncio.current_task().get_name()}】业务办理完毕")


async def main():
    tasks = [
        asyncio.create_task(bank(), name=f"银行柜台==={item}===") for item in range(10)
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
