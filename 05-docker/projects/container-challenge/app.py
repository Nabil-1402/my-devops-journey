from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello_world():
    return 'Welcome to the CoderCo Containers Challenge'

@app.route('/count')
def icount():
    count= redis.incr('hits')
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)