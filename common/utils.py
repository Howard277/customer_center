import time


# 获取当前时间的字符串形式
def get_time_str():
    return time.strftime('%Y-%m-%D %H:%M:%S', time.localtime())


# 获取sql中的count的情况
def get_sql_count(table_name):
    return str.format('select count(1) from %s ', table_name)


# 获取sql中all的情况
def get_sql_all(table_name):
    return str.format('select all from %s ', table_name)


# 获取sql中的limit
def get_sql_limit(page):
    page_size = 10
    current_page = 1
    if 'page_size' in page:
        page_size = page['page_size']
    if 'current_page' in page:
        current_page = page['current_page']
    start_position = (current_page - 1) * page_size
    end_position = current_page * page_size
    return str.format(' limit %d %d ', start_position, end_position)
