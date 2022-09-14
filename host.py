from flask import Flask

server = Flask(__name__)

@server.route('/')
def index():
  return 'Welcome'
server.run(debug=True, host=0.0.0.0)
