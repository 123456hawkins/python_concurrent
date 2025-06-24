# 异步迭代器
# 异步上下文管理
import asyncio

import time


class DistributedTaskManager:
    class Node:
        def __init__(self, key):
            self.key = key
            self.next: DistributedTaskManager.Node | None = None

    def __init__(self) -> None:
        self.__root = None
        self.__lase = None

    def add_task_key(self, key):
        new_node = DistributedTaskManager.Node(key)
        if self.__root is None:  # 没有根节点
            self.__root = new_node  # 设置根节点
            self.__last = new_node  # 设置最后一个节点
        else:
            self.__last.next = new_node
            self.__last = self.__last.next

    def __aiter__(self):
        self.__current = self.__root
        return self

    async def __anext__(self):  # 下一个数据
        if self.__current == None:  # 没有数据
            raise StopAsyncIteration()  # 结束异步迭代
        key = self.__current.key  # 获取当前节点的key
        value = await self.task_server_search(key)
        self.__current = self.__current.next  # 移动到下一个节点
        return key, value

    async def task_server_search(self, task_key):  # 消息回应处理
        await asyncio.sleep(2)
        if task_key == "java":
            return "java并发编程"
        elif task_key == "python":
            return "python并发编程"
        else:
            return "未知编程语言"


import asyncio
import time


# DistributedTaskManager 类的定义保持不变
class DistributedTaskManager:
    class Node:
        def __init__(self, key):
            self.key = key
            self.next: DistributedTaskManager.Node | None = None

    def __init__(self) -> None:
        self.__root = None
        self.__last = None
        self.__keys = []  # 为了方便并发，我们直接用列表存储key

    def add_task_key(self, key):
        self.__keys.append(key)

    async def task_server_search(self, task_key):
        await asyncio.sleep(2)
        if task_key == "java":
            return task_key, "java并发编程"
        elif task_key == "python":
            return task_key, "python并发编程"
        else:
            return task_key, "未知编程语言"

    def get_all_keys(self):
        return self.__keys


async def main():
    task_manager = DistributedTaskManager()
    start_time = time.time()

    task_manager.add_task_key("java")
    task_manager.add_task_key("python")
    task_manager.add_task_key("javascript")

    # 1. 创建所有任务的协程对象，但不要 await
    tasks_to_run = []
    for key in task_manager.get_all_keys():
        # asyncio.create_task() 会立即将任务提交给事件循环去执行
        task = asyncio.create_task(task_manager.task_server_search(key))
        tasks_to_run.append(task)

    # 2. 使用 asyncio.gather() 并发运行所有任务并等待它们全部完成
    #    这三个任务会“同时”开始，都在后台 sleep(2)。
    #    gather 会等待最长的那个任务完成，由于它们都是2秒，所以总等待时间是2秒。
    results = await asyncio.gather(*tasks_to_run)

    # 3. 处理已完成的结果
    for key, value in results:
        print(f"【任务处理】任务键: {key}, 任务值: {value}")

    end_time = time.time()
    print(f"【任务处理】总耗时: {end_time - start_time:.2f}秒")


if __name__ == "__main__":
    asyncio.run(main())
