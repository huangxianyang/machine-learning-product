# -*- utf-8 -*-
"""
服务主程序
"""
import sys
sys.path.append('..')

from flask import Flask, request, jsonify
from waitress import serve
import os
from general_model.handler import handle

app = Flask(__name__)

class Event:
    def __init__(self):
        self.body = request.get_data()
        self.headers = request.headers
        self.method = request.method
        self.query = request.args
        self.path = request.path

class Context:
    def __init__(self):
        self.hostname = os.environ['HOSTNAME'] # LOGNAME, HOSTNAME
        self.version  = '0.0.1' # 版本号


def format_status_code(resp):
    if 'statusCode' in resp:
        return resp['statusCode']

    return 200


def format_body(resp):
    if 'body' not in resp:
        return ""
    elif type(resp['body']) == dict:
        return jsonify(resp['body'])
    else:
        return str(resp['body'])


def format_headers(resp):
    if 'headers' not in resp:
        return []
    elif type(resp['headers']) == dict:
        headers = []
        for key in resp['headers'].keys():
            header_tuple = (key, resp['headers'][key])
            headers.append(header_tuple)
        return headers

    return resp['headers']


def format_response(resp):
    if resp == None:
        return ('', 200)

    statusCode = format_status_code(resp)
    body = format_body(resp)
    headers = format_headers(resp)
    return (body, statusCode, headers)


@app.route('/gsm', methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE']) # 通用评分模型(General score model)
def call_handler():
    event = Event()
    context = Context()
    response_data = handle(event,context)
    resp = format_response(response_data)
    return resp

if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5009,debug=True)
    serve(app, host='0.0.0.0', port=5009)
