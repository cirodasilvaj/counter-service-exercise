from flask import Flask
app = Flask(__name__)
count = 0
@app.route("/")
def index(): return "counter-service"
@app.route("/count")
def inc():
    global count; count += 1
    return {"count": count}
if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)
