import multiprocessing

# 管道传输


def message_send(connect, msg):
    print("【数据发送】", msg)
    connect.send(msg)


def message_receive(connect):
    print("【数据接收】%s" % connect.recv())


def main():
    # 创建管道会返回两个对象，输入管道和输出管道
    connect_receive, connect_send = multiprocessing.Pipe()
    # 管道创建完成后，就根据管道来创建进程，每一个进程处理函数之中都需要接收管道对象
    process_send = multiprocessing.Process(
        target=message_send,
        args=(
            connect_send,
            "hell from hawkins",
        ),
    )
    process_receive = multiprocessing.Process(
        target=message_receive, args=(connect_receive,)
    )
    process_send.start()
    process_receive.start()

    # 等待子进程结束
    process_send.join()
    process_receive.join()
    print("【管道通信处理完毕】")


if __name__ == "__main__":
    main()
