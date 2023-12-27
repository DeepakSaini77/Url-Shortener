from flask import Flask, redirect, request, jsonify, abort
from flask_cors import CORS
import hashlib
import redis

app = Flask(__name__)
CORS(app)  
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def home():
    return 'URL Shortener Service is running.'

@app.route('/generate', methods=['POST'])
def generate_hashed_url():
    long_url = request.json['long_url']
    hash_object = hashlib.sha1(long_url.encode())
    hash_value = hash_object.hexdigest()[:16] 
    hashed_url = f"http://127.0.0.1:5000/{hash_value}"

    redis_client.set(hash_value, long_url)

    redis_client.expire(hash_value, 24 * 60 * 60)

    return {'hashed_url': hashed_url}

@app.route('/<hash_value>')
def click_tracking(hash_value):
    if redis_client.exists(hash_value):
        click_count_key = f"{hash_value}:click_count"
        click_count = redis_client.incr(click_count_key)

        if click_count > 2:
            redis_client.delete(hash_value)
            redis_client.delete(click_count_key)
            return abort(404)

        original_url_bytes = redis_client.get(hash_value)

        if original_url_bytes is not None:
            original_url = original_url_bytes.decode('utf-8')
            print(f"Click tracked for {original_url}")
            return redirect(original_url)
    else:
        return abort(404)

if __name__ == '__main__':
    app.run(debug=True)