from flask import Flask, redirect, request, jsonify, abort
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)  
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def home():
    return 'URL Shortener Service is running.'

if __name__ == '__main__':
    app.run(debug=True)
