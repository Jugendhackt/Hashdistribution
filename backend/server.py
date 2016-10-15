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
    passwd = request.args.get('passwd')
    cmd = request.args.get('cmd')
    if (cmd == "clear_cache"):
        os.system("rm /home/pi/Hashdistribution/backend/.cache/*")
        return '<center><h4>Cache geleert!</h4></center>'
    return 'Client IP: ' + ip + '<hr>Commands:<br><li>?cmd=clear_cache&passwd=12345</li>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
