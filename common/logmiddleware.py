from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest
import logging
import json


# 日志 中间件 类
class LogMiddleware(MiddlewareMixin):
    # 处理函数
    def process_request(self, request):
        # 记录请求的方法和地址
        method = request.method
        path = request.path
        infos = {'method': method, 'path': path}
        # POST请求数据也要记录
        if method == 'POST':
            if request.content_type == 'application/json':
                infos['data'] = json.loads(request.body.decode())
            else:
                infos['data'] = request.POST
        print(infos)
        pass
