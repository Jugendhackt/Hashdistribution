from flask import Flask, jsonify, request, send_from_directory
import os
import crawler
import TweetReader

app = Flask(__name__, static_url_path='')

@app.route('/')
def all():
    ip = request.remote_addr
    callback = request.args.get('callback')
    hashtag = request.args.get('hashtag')
    depth = request.args.get('depth')
    #crawler.getjson(hashtag)
    json = TweetReader.getTopHashtags(hashtag, depth)
    return json

@app.route('/debug')
def debug():
    ip = request.remote_addr
    list = os.listdir("/home/pi/Hashdistribution/backend/.cache/") # dir is your directory path
    cache_status = len(list)
    return '<b>Client IP:</b> ' + ip + '<hr><b>Cache:</b> ' + str(cache_status) + ' Dateien<hr>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
