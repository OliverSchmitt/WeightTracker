import flask


server = flask.Flask(__name__)


@server.route("/")
def index():
    return flask.render_template("index.html")

@server.route("/enter")
def enter():
    return flask.render_template("enter.html")

@server.route("/weight_entered", methods=["POST"])
def weight_entered():
    return flask.render_template("weight_entered.html", weight=flask.request.form["weight"])


if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0")
