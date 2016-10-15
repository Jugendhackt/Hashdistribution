from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def all():
    ip = request.remote_addr
    callback = request.args.get('callback')
    hastag = request.args.get('hashtag')
    depth = request.args.get('depth')
    return '{0}({1})'.format(callback, {'client_ip':ip,'b':2,'hastag':hastag,'depth':depth})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
