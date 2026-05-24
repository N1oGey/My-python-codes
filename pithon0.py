from flask import Flask, request
import webbrowser

app = Flask(__name__)

ACTIVATION_CODE = "1234"

@app.route("/open")
def open_link():
    code = request.args.get("code")
    url = request.args.get("url")

    if code == ACTIVATION_CODE:
        webbrowser.open(url)
        return "OK"

    return "DENIED"

app.run(host="0.0.0.0", port=5000)