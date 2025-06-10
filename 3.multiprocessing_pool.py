# 进程池
import multiprocessing, time


def process_task(item):
    if item % 10 == 2:
        raise NotImplementedError("业务异常")
    time.sleep(0.5)
    return f'"{multiprocessing.current_process().name}"进程,业务处理步骤：{item}'


def process_task_callback(result):
    print(f"回调函数处理结果：{result}")


def process_error_callback(error):
    print(f"回调函数处理异常：{error}")


def main():
    process_pool = multiprocessing.Pool(
        processes=multiprocessing.cpu_count() * 2
    )  # 设置进程池大小为CPU核心数

    for item in range(500):
        # 循环创建进程
        result = process_pool.apply_async(
            func=process_task,
            args=(item,),
            callback=process_task_callback,
            error_callback=process_error_callback,
        )
        # 以下代码会阻塞子进程
        # try:
        #     # 获取结果，如果进程执行异常，则会抛出异常
        #     result.get()  # 设置超时时间为3秒,此代码会阻塞子进程
        # except Exception as e:
        #     print(f"获取结果异常：{e}")
        #     continue
    process_pool.close()  # 关闭进程池，不再接受新的任务

    process_pool.join()  # 等待所有子进程执行完毕
    print("【进程池处理完毕】")


if __name__ == "__main__":
    main()
