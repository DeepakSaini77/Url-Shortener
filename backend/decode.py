from flask import redirect, abort
from main import app, redis_client


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
