# 证明多线程不适用于cpu密集型
import threading
import time


# 一个耗时的计算任务，代替原来的 time.sleep()
def cpu_bound_worker():
    """这是一个CPU密集型任务，会进行大量计算"""
    print(f"线程 {threading.current_thread().name} 开始计算...")
    total = 0
    # 执行一个大循环来进行密集计算
    for i in range(100_000_000):
        total += i
    print(f"线程 {threading.current_thread().name} 计算结束.")


def run_single_thread():
    """单线程执行"""
    print("--- 开始单线程测试 ---")
    start_time = time.perf_counter()
    cpu_bound_worker()
    end_time = time.perf_counter()
    print(f"【单线程】执行耗时: {end_time - start_time:.2f} 秒\n")


def run_multi_thread(num_threads=4):
    """多线程执行"""
    print(f"--- 开始 {num_threads} 个线程测试 ---")
    threads = []
    for i in range(num_threads):
        # 创建多个线程，都执行CPU密集型任务
        thread = threading.Thread(target=cpu_bound_worker, name=f"CPU线程{i+1}")
        threads.append(thread)

    start_time = time.perf_counter()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.perf_counter()
    print(f"【{num_threads}个线程】执行耗时: {end_time - start_time:.2f} 秒")


if __name__ == "__main__":
    # 先跑单线程
    run_single_thread()
    # 再跑多线程（例如4个线程）
    run_multi_thread(num_threads=4)
