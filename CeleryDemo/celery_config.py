# coding: utf-8


# 使用redis作为消息代理
BROKER_URL = 'redis://127.0.0.1:6379/0'
# 结果存储在Redis
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# 任务序列化和反序列化使用msgpack方案，比json高效
CELERY_TASK_SERIALIZER = 'json'
# 读取结果时序列化方案
CELERY_RESULT_SERIALIZER = 'json'
# 任务过期时间
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 指定接受的内容类型
CELERY_ACCEPT_CONTENT = ['json',]