from flask import Flask
import os
import redis

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)


@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
        return (
            f'<h1>Witaj w GitHub Cloud!</h1>'
            f'<p>Odwiedzono te strone <b>{count}</b> razy.</p>'
        )
    except Exception:
        return "Oczekuje na polaczenie z baza Redis..."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
