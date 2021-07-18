from flask import Flask, request


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return "hello its from POST"
    else:
        return "Hello its from Get"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 2021)