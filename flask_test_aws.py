from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def howdy():
    return f"Howdy Folks {random.randint(0,100)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)