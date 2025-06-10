import multiprocessing, time


# 守护进程
def process_core():
    # 守护进程由子进程创建，子进程结束时，守护进程会自动结束
    daemon_process = multiprocessing.Process(
        target=process_check, name="守护进程", daemon=True
    )
    daemon_process.start()  # 启动守护进程
    for item in range(2):
        print(
            "【业务处理】进程ID:%s、进程名称:%s;当前处理阶段:%d"
            % (
                multiprocessing.current_process().pid,
                multiprocessing.current_process().name,
                item + 1,
            )
        )
        time.sleep(2)


def process_check():
    count = 1
    while True:
        print(f"【守护进程】第{count}次检查")
        count += 1
        time.sleep(1)


def main():
    process = multiprocessing.Process(target=process_core, name="hawkins业务进程")
    process.start()
    process.join()  # 等待子进程处理完毕再继续执行主进程,不加join()方法，主进程会直接结束
    print("【进程处理完毕】")


if __name__ == "__main__":
    main()
