from flask import Flask
from flask import jsonify
from dotenv import dotenv_values
from flask import request
from .controllers import sum_operation

app = Flask(__name__)


@app.route("/")
def server_info() -> str:
    return "My Server"


@app.route("/author")
def author():
    config = dotenv_values(".env")
    author_data = {
        "name": config["AUTHOR_NAME"],
        "course": config["AUTHOR_COURSE"],
        "age": config["AUTHOR_AGE"]
    }
    return jsonify(author_data)


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return int(config["PORT"])
    return 5000


def debug_status() -> bool:
    config = dotenv_values(".env")
    if "DEBUG" in config:
        return bool(config["DEBUG"])
    return False


@app.route("/sum")
def sum_calculation():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({"sum": sum_operation(a, b)})


if __name__ == "__main__":
    app.run(debug=debug_status(), port=get_port())
