import socket
import datetime
from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():

    writeInLog("log")
    string = logToString("log")
    return "Salut Monde! Greetings from "+socket.gethostname()+"\n\n"+string+"\n"


if __name__ == "__main__":
    application.run()


def writeInLog(logfile):
    file = open(logfile, "w")
    file.write("Host: "+socket.gethostname()+"  Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())+"\n")
    file.close()

def logToString(logfile):
    file = open(logfile, "r")
    return file.read()
