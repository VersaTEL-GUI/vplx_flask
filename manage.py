# coding:utf-8

from flask import Flask, jsonify, make_response
import subprocess


app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)

def is_master():
    with open('is_master', 'r')as f:
        result=f.read()
    return result

def corss_domain(datadict):
    response = make_response(jsonify(datadict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route('/login')
def login():
    data=is_master()
    return corss_domain(data)

@app.route('/data/<cmd>/', methods=['GET', 'POST'])
def cmd_data(cmd):
    data=subprocess.getoutput(cmd)
    return corss_domain(data)


app.run(host='0.0.0.0', port=12122)
