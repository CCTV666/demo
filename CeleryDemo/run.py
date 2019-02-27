from celery_app import *

import time


# from celery.task.control import revoke

def main():
    # res = add.delay(1, 2)
    #
    # print(res)
    # print(res.result)
    # # revoke(res, terminate=True)
    result = add.delay(1, 2)
    time.sleep(10)
    # revoke(result.id, terminate=True, signal="kill")
    print(result.id)
    stop_task(result.id)

    print(result.ready())


def main1():
    result = print_message.delay()
    time.sleep(10)


def main2():
    result = test.delay()
    time.sleep(10)
    stop_task(result.id)

    print(result.ready())

    add.delay(1, 2)


def main3():
    result = write.delay()
    print(f"xxx{result.id}")
    time.sleep(3)
    stop_task(result.id)


if __name__ == '__main__':
    main3()
    # stop_task("2bfa25f9-2c65-43ba-b480-ceafa1ee187e")
