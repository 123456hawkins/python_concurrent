import threading
import time


def worker(delay):
    for num in range(10):
        time.sleep(delay)
        print("[%s]线程执行计数%s" % (threading.current_thread().name, num))


def main():
    work_threads = [
        threading.Thread(target=worker, args=(1,), name=f"[工作线程{item}]")
        for item in range(10)
    ]
    for thread in work_threads:
        thread.start()  # 启动线程
    for thread in work_threads:
        thread.join()  # 等待线程结束
    print("【线程处理完毕】")


if __name__ == "__main__":
    main()
