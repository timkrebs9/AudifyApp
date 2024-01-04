import jwt
import datetime
import os
from flask import Flask, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv

# .env-Datei laden
load_dotenv()

server = Flask(__name__)
mysql = MySQL(server)

# Konfigurieren Sie den Server mit Umgebungsvariablen
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = int(os.environ.get("MYSQL_PORT") or 3306)  # Standardwert auf 3306 setzen, falls nicht definiert

@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    
    if not auth:
        return "missing credentials", 401

    # check db for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username,)
    )