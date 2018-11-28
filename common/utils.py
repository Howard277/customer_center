import time


# 获取当前时间的字符串形式
def get_time_str():
    return time.strftime('%Y-%m-%D %H:%M:%S', time.localtime())
