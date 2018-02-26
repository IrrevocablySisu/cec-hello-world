import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Salut Monde! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
