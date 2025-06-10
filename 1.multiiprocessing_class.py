import multiprocessing
import time


class ProcessCore(multiprocessing.Process):
    def __init__(self, **kwargs):
        super().__init__(name=kwargs.get("name"))
        self.__delay = kwargs.get("delay")
        self.__count = kwargs.get("count")

    # 进程的起点方法
    def run(self):
        for num in range(self.__count):
            print(
                "【count=%d】进程ID:%s、进程名称:%s"
                % (
                    num,
                    multiprocessing.current_process().pid,
                    multiprocessing.current_process().name,
                )
            )
            time.sleep(self.__delay)


def main():
    for item in range(3):
        process = ProcessCore(name=f"hawkins处理进程-{item}", delay=1, count=5)
        # 不能直接调用类中的run()方法，因为run()方法只是定义了进程的执行业务逻辑，并不包含底层启动逻辑
        # Python之中的进程启动依靠Python虚拟机与操作系统交互而实现，而start()实现的就是这样的交互
        # start()方法与操作系统调用完成之后，会自动调用run()方法
        process.start()


if __name__ == "__main__":
    main()
