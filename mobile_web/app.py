#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect
from flask import render_template

app = Flask(__name__)

update_data = """
{
  "msg":"update info",
  "pn":"",
  "vc":"1000000",
  "vn":"1.0.0-SNAPSHOT",
  "download_url":"",
  "channel":"dakehu",
  "extra":"",
  "force": 0
}"""


@app.route('/mobile/native/user_info')
def api_app_download():
    return render_template('mobile-user-info.html')


@app.route('/kmobile/app/download', methods=['GET'])
def band_app_download():
    if request.method == 'GET':
        return render_template('kmobile-app-download.html')
    else:
        return '<h1>only support method GET！</h1>'


@app.route('/api/v1/app/update', methods=['GET', 'POST'])
def api_app_update():
    if request.method == 'GET':
        a = request.get_data()
        update_json_obj = json.loads(update_data)
        # return json.dumps(update_json_obj["data"])
        return jsonify(update_json_obj)
    else:

        return '<h1>only support method GET！</h1>'


# just download at /static/<filename>
@app.route('/<filename>')
def download(filename):
    return None


@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=17779,
        debug=True
    )
