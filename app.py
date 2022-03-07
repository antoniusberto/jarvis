from flask import Flask, request, make_response, render_template, Response, jsonify


app = Flask(__name__)

@app.route("/jarvis", methods=["GET", "POST"])
def jarvis():
    print("entrou hein")
    return make_response("", 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

    print ("thread finished...exiting")
