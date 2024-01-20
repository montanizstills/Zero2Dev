from flask import Flask

app = Flask(__name__)


@app.route('/hello-world', methods=["GET"])
def hello_world():
    return 'Hello World!'


@app.route('/zero2dev/jira/webhooks/newUserAccepted', methods=["GET"])
def user_accepted():
    return '\n Zero2Dev has just confirmed a new user. \n'


if __name__ == '__main__':
    # self-hosted TSL security
    # app.run(ssl_context=('./zero2dev-cert.pem', './zero2dev.pem'))

    # incoming connection mask # 0.0.0.0 means anywhere
    app.run(host="0.0.0.0")
