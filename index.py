from flask import Flask, jsonify, request, send_file
from code_spider import CodeSpider

from login_spider import LoginSpider

app = Flask(__name__)


@app.route('/auth_get', methods=['GET'])
def auth_get():
    return jsonify(CodeSpider().run())

@app.route('/auth_post', methods=['POST'])
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

@app.route('/image/<imageid>', methods=['GET'])
def image(imageid):
    return send_file("static/code_img/{}.gif".format(imageid))

if __name__ == '__main__':
    app.debug = True
    app.run()
