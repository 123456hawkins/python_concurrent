# 多协程
import time


def message_producer(author, book, consumer):
    message = None
    # 在使用yield进行手工协程实现的时候，一定要先发送一个空消息
    consumer.send(message)
    for i in range(3):
        message = f"作者: {author}, 书名: {book}"
        time.sleep(1)
        print("【生产者】%s" % message)
        consumer.send(message)


def message_consumer():
    while True:
        message = yield
        print("【消费者】%s" % message)


def main():
    consumer = message_consumer()
    message_producer("hawkins", "python并发编程", consumer)


if __name__ == "__main__":
    main()
