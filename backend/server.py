from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def all():
    ip = request.remote_addr
    callback = request.args.get('callback')
    hastag = request.args.get('hashtag')
    depth = request.args.get('depth')
    return '{0}({1})'.format(callback, {'client_ip':ip,'hastag':hastag,'depth':depth})

@app.route('/debug')
def debug():
    ip = request.remote_addr
    list = os.listdir("/home/pi/Hashdistribution/backend/.cache/") # dir is your directory path
    cache_status = len(list)
    return 'Client IP: ' + ip + 'Cache: ' + str(cache_status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
