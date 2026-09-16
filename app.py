from flask import Flask, jsonify

app = Flask(__name__)
count = 0


@app.route("/count")
def get_count():
    global count
    count += 1
    return jsonify(count=count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
