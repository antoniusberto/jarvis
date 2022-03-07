from flask import Flask, request, make_response, render_template, Response, jsonify


app = Flask(__name__)

@app.route("/jarvis", methods=["GET", "POST"])
def jarvis():
    print("entrou hein")
