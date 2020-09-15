# coding:utf-8

from flask import Flask, jsonify, make_response
import subprocess


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
    :param datadict: 页面返回的数据
    :return: response
    '''
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route('/is_master')
def is_master():
    data=read_flag_file()
    return corss_domain(data)

@app.route('/data/<cmd>/', methods=['GET', 'POST'])
def cmd_result(cmd):
    data=subprocess.getoutput(cmd)
    return corss_domain(data)


app.run(host='0.0.0.0', port=12122)
