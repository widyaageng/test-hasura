#type: ignore
from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.post('/alerts')
def alerts():
    body = request.get_json()
    print(body)
    return { 'status': 'Created'}, 201

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8001)