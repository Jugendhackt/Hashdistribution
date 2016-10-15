from flask import Flask, jsonify, request

@app.route('/')
def all():
    temp1 = 23.5
    temp2 = 21.2
    ip = request.remote_addr
    callback = request.args.get('callback')
    return '{0}({1})'.format(callback, {'client_ip':ip,'b':2,'temp1':temp1,'temp2':temp2})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
