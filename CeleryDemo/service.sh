#!/usr/bin/env bash

stop() {
    ps -ef|grep celery|grep -v grep |awk '{print $2}'|xargs kill -9
    echo "service stopped"
}

start() {
    nohup python3 celery -A celery_app worker -l info >> celery.log 2>&1 &
    nohup python3 celery -A celery_app beat >> celery_beat.log 2>&1 &
    echo "service started"
}

restart() {
    stop
    sleep 2
    echo "restarting..."
    start
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    *)
        echo "Usage: {start|stop|restart}"
        exit 1
esac
exit 0