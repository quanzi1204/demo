from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return "hello"

if __name__ == '__main__':
    app.run(port=5000, debug=True)