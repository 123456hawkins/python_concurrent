# 多协程
import time
import gevent

# 全局变量
message = None


def message_producer(author, book):
    global message
    for i in range(3):
        message = f"作者: {author}, 书名: {book}"
        time.sleep(1)
        print("【生产者】%s" % message)
        # 协程切换延迟
        gevent.sleep(1)


def message_consumer():
    while True:
        print("【消费者】%s" % message)
        gevent.sleep(1)  # 模拟处理时间，避免过快消费


def main():
    producer_gevent = gevent.spawn(message_producer, "hawkins", "python并发编程")
    consumer_gevent = gevent.spawn(message_consumer)
    producer_gevent.join()  # 等待生产者完成
    consumer_gevent.kill()  # 停止消费者协程


if __name__ == "__main__":
    main()
