import multiprocessing

# 数据共享


def message_send(data, key, value):
    data.update({key: value})


def main():
    manager = multiprocessing.Manager()  # 创建一个Manager对象
    # 此时的字段是一个使用于多进程共享操作的字典结构
    process_dict = manager.dict(author="hawkins")
    process_a = multiprocessing.Process(
        target=message_send,
        args=(
            process_dict,
            "sex",
            "male",
        ),
    )
    process_b = multiprocessing.Process(
        target=message_send,
        args=(
            process_dict,
            "age",
            18,
        ),
    )
    process_a.start()
    process_b.start()
    process_a.join()
    process_b.join()
    print("【数据共享处理完毕】", process_dict)


if __name__ == "__main__":
    main()
