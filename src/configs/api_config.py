# !/usr/bin/python3
# coding: utf-8
# @Author: lixiang
# @Date: 2023-12-27

## 设置API启动所需的参数与变量
def app_config(_app):
    ## 设置封面数据加载路径
    _app.config['LOAD_ROOT_COVER'] = 'load/cover_imgs'
    _app.config['LOAD_ROOT_BOOKS'] = 'load/books'


    _app.config['BASE_URL'] = "http://106.13.248.184:8088"

    _app.config['COVER_URL'] = "http://106.13.248.184:8088/data/cover_pic"
    _app.config['PAGE_URL']  = "http://106.13.248.184:8088/data/page_pic"
    _app.config['AUDIO_URL']  = "http://106.13.248.184:8088/data/page_audio"

    ## 设置三维重建项目输出结果存放路径
    _app.config['RESULTS_FOLDER'] = './Final_out/'

    ## 设置进程运行标志, True表示任务正在运行中，拒绝新的请求；False表示无任务运行，可接收新的请求
    _app.config['RUN_FLAG'] = False

    ## 设置请求接口地址, 时间日志打点
    _app.config['SAVE_LOG_URL'] = "http:///test-api-ai.moviebook.com/api/technology/savelog"

    ## 设置结果回调接口地址
    _app.config['CALLBACK_URL'] = "http://api-ai.moviebook.com/api/task/callback"

    ## 设置允许上传的文件格式
    _app.config['ALLOW_EXTENSIONS'] = ['zip',]
    
    return _app