import socket
import datetime
from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():

    write_in_log("/mnt/log/logs/log.txt")
    log = log_to_string("log.txt")
    hello_world = "Hello World ! <br><br>"
    final_string = hello_world+log

    return final_string


if __name__ == "__main__":
    application.run()


def write_in_log(logfile):
    file = open(logfile, "w")
    file.write("Host: "+socket.gethostname()+"  Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())+"\n")
    file.close()


def log_to_string(logfile):
    file = open(logfile, "r")
    string = file.read()
    file.close()

    return string
