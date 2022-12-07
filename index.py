from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def getWelcome():
    return {
        "test":1
    }

if __name__ == "__main__":
    app.run()   