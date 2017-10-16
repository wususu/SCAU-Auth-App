from flask import Flask, jsonify, request, send_file, make_response
from functools import wraps
from code_spider import CodeSpider

from login_spider import LoginSpider

app = Flask(__name__)

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


@app.route('/auth/get', methods=['GET'])
@allow_cross_domain
def auth_get():
    return jsonify(CodeSpider().run())

@app.route('/auth/post', methods=['POST'])
@allow_cross_domain
def auth_post():
    session = request.values.get('session')
    view_state = request.values.get('view_state')
    username = request.values.get('username')
    passwd = request.values.get('passwd')
    code = request.values.get('code')
    if session is None or view_state is None or username is None or passwd is None or code is None:
        return jsonify(LoginSpider.error)
    print(session, " ", view_state, " ", username," ",passwd," ",code)
    return jsonify(LoginSpider(number=username, passwd=passwd, session=session, view_state=view_state, code=code).run())

@app.route('/auth/image/<imageid>', methods=['GET'])
@allow_cross_domain
def image(imageid):
    return send_file("static/code_img/{}.gif".format(imageid))

if __name__ == '__main__':
    app.debug = True
    app.run()
