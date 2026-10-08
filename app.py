from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/zero2dev/hello-world', methods=["GET"])
def hello_world():
    return 'Hello Zero2Dev!'


@app.route('/zero2dev/jira/webhooks/newUserAccepted', methods=["POST"])
def user_accepted():
    # A user is only created one time, if ever suspended
    # the next time that same user (email) is invited, and it is
    # accepted, this SHOULD count as user `updated`.

    # TODO - BUG: endpoint being hit when user is suspended.
    return '\n Zero2Dev has just confirmed a new user. \n'


@app.route('/zero2dev/jira/webhooks/userUpdated', methods=["POST"])
def user_updated():
    # If user is updated, get history (tasks/stories) remaining
    # for this user to create.
    return ""


@app.route('/zero2dev/jira/webhooks/userDeleted', methods=["POST"])
def user_deleted():
    # If and when a user is deleted, we need to know
    # which remaining stories for this user to complete and
    # place in DynamoDB or some other persistence engine.
    return ""


if __name__ == '__main__':
    # self-hosted TSL security
    # app.run(ssl_context=('./zero2dev-cert.pem', './zero2dev.pem'))

    # incoming connection mask # 0.0.0.0 means anywhere
    app.run(host="0.0.0.0")
