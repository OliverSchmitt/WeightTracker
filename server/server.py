import flask

import server


flask_server = flask.Flask(__name__)


@flask_server.route("/")
def index():
    return flask.render_template("index.html")

@flask_server.route("/enter")
def enter():
    return flask.render_template("enter.html")

@flask_server.route("/weight_entered", methods=["POST"])
def weight_entered():
    weight = flask.request.form["weight"]
    server.insert_weight(weight)
    return flask.render_template("weight_entered.html", weight=weight)


if __name__ == "__main__":
    flask_server.run(debug=True, host="0.0.0.0")
