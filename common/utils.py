import time
import redis
from redis.sentinel import Sentinel
from customer_center import settings


# 获取当前时间的字符串形式
def get_time_str():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def get_date_str():
    return time.strftime('%Y-%m-%d', time.localtime())


def get_time_str2():
    return time.strftime('%Y%m%d%H%M%S', time.localtime())


def get_date_str2():
    return time.strftime('%Y%m%d', time.localtime())


# 获取sql中的count的情况
def get_sql_count(table_name):
    return str.format('select count(1) from %s ', table_name)


# 获取sql中all的情况
def get_sql_all(table_name):
    return str.format('select all from %s ', table_name)


# 获取redis 哨兵
def _get_redis_sentinel():
    return Sentinel(settings.REDIS_SENTINELS,
                    socket_timeout=10)


# 获取redis master
def get_redis_master():
    sentinel = _get_redis_sentinel()
    master = sentinel.discover_master('mymaster')
    return sentinel.master_for(settings.REDIS_SERVICE_NAME, socket_timeout=0.5, password=settings.REDIS_PASSWORD,
                               db=settings.REDIS_DB)


# 获取redis slave
def get_redis_slave():
    sentinel = _get_redis_sentinel()
    # master = sentinel.discover_master('mymaster')
    return sentinel.slave_for(settings.REDIS_SERVICE_NAME, socket_timeout=0.5, password=settings.REDIS_PASSWORD,
                              db=settings.REDIS_DB)[0]


# redis自增
def redis_incr(key):
    redis_instance = get_redis_master()
    id_primary = key + get_date_str2()  # redis中存储的key是传入的关键字加当前日期信息。
    id_increase = redis_instance.incr(id_primary)
    return id_primary + str(id_increase)  # 最终返回信息为redis中存储的key+value


print(redis_incr('test'))
