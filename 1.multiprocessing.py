import multiprocessing
import time


def process_core(delay, count):
    for num in range(count):
        print(
            "【count=%d】进程ID:%s、进程名称:%s"
            % (
                num,
                multiprocessing.current_process().pid,
                multiprocessing.current_process().name,
            )
        )
        time.sleep(delay)  # 模拟处理延时,人为阻塞状态


def main():
    print(
        "【主进程】进程ID:%s、进程名称:%s"
        % (
            multiprocessing.current_process().pid,
            multiprocessing.current_process().name,
        )
    )
    for item in range(3):
        process = multiprocessing.Process(
            target=process_core,
            args=(
                1,
                60,
            ),
            name=f"Hawkns业务处理进程-{item}",  # 进程名称
        )
        process.start()


if __name__ == "__main__":
    main()
