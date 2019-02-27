from celery import Celery
import pymysql
import time

app = Celery("MozheAPI")
app.config_from_object('celery_config')


@app.task
def add(x, y):
    for i in range(10):
        with open("t.txt", "w"
                           "", encoding="utf8") as fp:
            fp.write(str(i))
    return x + y


@app.task
def test():
    DATABASE = {
        'host': '192.168.40.13',
        'port': 3306,
        'user': 'root',
        'password': 'llzx',
        'db': 'test',
        'charset': 'utf8'
    }
    conn = pymysql.connect(**DATABASE)
    cursor = conn.cursor()
    for i in range(1000000):
        cursor.execute(f"INSERT INTO `CeleryDemo`(`key`) VALUES ({i});")
        conn.commit()
    conn.close()


@app.task
def print_message():
    for i in range(100000000):
        print(i)


def stop_task(task_id):
    print(f"stop: {task_id}")
    # app.AsyncResult(task_id).revoke()
    app.control.revoke(task_id, terminate=True, signal='SIGKILL')


def show_activate_task():
    app.task.control.inspect().active()


@app.task
def write():
    with open("file1.txt", "w", encoding="utf8") as fp:
        fp.write("file1")
    time.sleep(10)
    with open("file2.txt", "w", encoding="utf8") as fp:
        fp.write("file2")


if __name__ == '__main__':
    app.start()
