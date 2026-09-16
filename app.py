from flask import Flask, jsonify

app = Flask(__name__)
counter = 0


@app.route("/")
def index():
    global counter
    counter += 1
    return jsonify(counter=counter)


@app.route("/reset")
def reset():
    global counter
    counter = 0
    return jsonify(counter=counter)


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
