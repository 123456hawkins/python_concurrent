import multiprocessing, time


def process_core():
    print("开始睡眠")
    time.sleep(2)  # 模拟处理延时,人为阻塞状态
    print(
        "【业务处理】进程ID:%s、进程名称:%s"
        % (
            multiprocessing.current_process().pid,
            multiprocessing.current_process().name,
        )
    )


def main():
    process = multiprocessing.Process(
        target=process_core,
        name=f"Hawkns业务处理进程",  # 进程名称
    )
    process.start()  # 子进程启动
    time.sleep(1)
    if process.is_alive():
        print("【进程中断执行】")
        process.terminate()
    print("【进程处理完毕】")


if __name__ == "__main__":
    main()
