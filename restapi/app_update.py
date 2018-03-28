#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect

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


@app.route('/band/v1/app/update', methods=['GET', 'POST'])
def band_app_update():
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


@app.route('/', methods=['GET'])
def index():
    return '<h1>hello ！</h1>'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=17778,
        debug=True
    )
