# coding:utf-8

from flask import Flask, jsonify, make_response
import subprocess
import base64


app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)

def read_flag_file():
    '''
    读取is_master文件
    :return: 0/1?None
    '''
    with open('is_master', 'r')as f:
        result=f.read()
    return result

def corss_domain(data):
    '''
    数据跨域
    :param data: 页面返回的数据
    :return: response
    '''
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route('/is_master')
def is_master():
    '''
    数据路由，判断master ip
    :return: 0/1?None
    '''
    data=read_flag_file()
    return corss_domain(data)

@app.route('/data/<cmd>/', methods=['GET', 'POST'])
def cmd_result(cmd):
    '''
    数据路由，接收cmd返回执行结果
    :param cmd: 用户输入命令
    :return: 执行结果
    '''
    cmd_str=base64.b64decode(cmd)
    print('result:', cmd_str, cmd)
    if subprocess.getstatusoutput(cmd_str):
        data=subprocess.getoutput(cmd_str)
        return corss_domain(data)
    else:
        str_err="错误命令无法执行"
        return corss_domain(str_err)


app.run(host='0.0.0.0', port=12122)
