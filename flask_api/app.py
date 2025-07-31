from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def pong(path):
    return "PONG", 200

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001)
