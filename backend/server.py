from flask import Flask, jsonify, request, send_from_directory
import os
import json

from flask import Response

import crawler
import TweetReader

app = Flask(__name__, static_url_path='')


@app.before_request
def option_autoreply():
    if request.method == 'OPTIONS':
        resp = app.make_default_options_response()

        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']

        h = resp.headers

        # Allow the origin which made the XHR
        h['Access-Control-Allow-Origin'] = request.headers['Origin']
        # Allow the actual method
        h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']
        # Allow for 10 seconds
        h['Access-Control-Max-Age'] = "10"

        # We also keep current headers
        if headers is not None:
            h['Access-Control-Allow-Headers'] = headers

        return resp


@app.after_request
def set_allow_origin(resp):
    h = resp.headers

    # Allow crossdomain for other HTTP Verbs
    if request.method != 'OPTIONS' and 'Origin' in request.headers:
        h['Access-Control-Allow-Origin'] = request.headers['Origin']

    return resp

@app.route('/', methods=['GET', 'OPTIONS'])
def all():
    #response.headers.add('Access-Control-Allow-Origin', '*')
    ip = request.remote_addr
    hashtag = request.args.get('hashtag')
    depth = request.args.get('depth')
    # crawler.getjson(hashtag)

    if (hashtag is not None) and (depth is not None):
        Json = TweetReader.getTopHashtags(hashtag, depth)
    else:
        return json.dumps('{ error:"Please add the arguments hashtag and depth" }')

    callback = request.args.get('callback')
    return Json


@app.route('/debug')
def debug():
    ip = request.remote_addr
    list = os.listdir(".cache/")  # dir is your directory path
    cache_status = len(list)
    return '<b>Client IP:</b> ' + ip + '<hr><b>Cache:</b> ' + str(cache_status) + ' Dateien<hr>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
