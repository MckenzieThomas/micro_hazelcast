from flask import Flask

app = Flask(__name__)

@app.route("/messages_service", methods=['GET'])
def messages_get():
    return "not implemented yet"

if __name__== "__main__":
    app.run(host="localhost",
            port=5005,
            debug=True)