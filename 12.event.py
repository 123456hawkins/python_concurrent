import asyncio

event = asyncio.Event()


async def passenger():
    print(f"【1】乘客等待公交车到站")
    await event.wait()
    print(f"【2】乘客上车，公交车开动了")


async def bus():
    await asyncio.sleep(3)
    event.set()


async def main():
    tasks = [
        asyncio.create_task(passenger(), name=f"乘客"),
        asyncio.create_task(bus(), name=f"公交车"),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
