from flask import Flask, request, session, redirect, url_for, abort


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.errorhandler(404)
def page_not_found(error):
    return {
        "error": "Please connect"
    }


@app.route("/connect", methods = ['POST'])
def connect():
    session['username'] = request.form['username']
    return {
        "method": "connect",
        "name_of_player": session['username']
    }


@app.route("/info", methods=['GET'])
def info():
    if 'username' in session:
        return {
            "method": "info",
            "name_of_player": session['username']
        }
    abort(404)


@app.route("/buy_raw", methods=['POST'])
def buy_raw():
    if 'username' in session:
        return {
            "method": "buy_raw",
            "name_of_player": session['username']
        }


@app.route("/sell_planes", methods=['POST'])
def sell_planes():
    if 'username' in session:
        return {
            "method": "sell_planes",
            "name_of_player": session['username']
        }


@app.route("/produce", methods=['POST'])
def produce():
    if 'username' in session:
        return {
            "method": "produce",
            "name_of_player": session['username']
        }


@app.route("/build", methods=['POST'])
def build():
    if 'username' in session:
        return {
            "method": "build",
            "name_of_player": session['username']
        }


@app.route("/finish", methods=['POST'])
def finish():
    if 'username' in session:
        return {
            "method": "finish",
            "name_of_player": session['username']
        }
