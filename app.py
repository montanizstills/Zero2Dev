from flask import Flask

app = Flask(__name__)


@app.route('/zero2dev/jira/webhooks/newUserAccepted', methods=["GET"])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run(ssl_context=('./zero2dev-cert.pem', './zero2dev.pem'))
    app.run()
