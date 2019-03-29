from flask import Flask, request
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route("/")
def hello():
    data = request.args.get('data')
    print(data)
    print("====================================")
    return "true"

app.run(host='0.0.0.0', port=3000, debug=False) 

