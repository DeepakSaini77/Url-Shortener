from flask import request, jsonify
from main import app, redis_client
import hashlib

@app.route('/generate', methods=['POST'])
def generate_hashed_url():
    long_url = request.json['long_url']
    hash_object = hashlib.sha1(long_url.encode())
    hash_value = hash_object.hexdigest()[:16] 
    hashed_url = f"http://127.0.0.1:5000/{hash_value}"

    redis_client.set(hash_value, long_url)

    redis_client.expire(hash_value, 24 * 60 * 60)

    return {'hashed_url': hashed_url}
