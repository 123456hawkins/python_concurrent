import multiprocessing, time


def process_core():

    time.sleep(5)  # 模拟处理延时,人为阻塞状态
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
    process.join()  # 等待子进程处理完毕再继续执行主进程,不加join()方法，主进程会直接结束
    print("【进程处理完毕】")


if __name__ == "__main__":
    main()
