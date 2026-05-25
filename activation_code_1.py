from flask import Flask, request
import webbrowser

app = Flask(__name__)

ACTIVATION_CODE = "1234"

@app.route("/open")
def open_link():
    code = request.args.get("code", "")
    url = request.args.get("url", "")

    if code == ACTIVATION_CODE and url:
        webbrowser.open(url)
        return "OK"
    return "DENIED"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)