import datetime
import json

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from pytz import timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/test_db"
db = SQLAlchemy(app, session_options={'autocommit': True})

# 클래스명이 테이블명
class User_test(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    inDt = db.Column(DateTime, default=datetime.datetime.now(timezone('Asia/Seoul')))

db.drop_all()
db.create_all()

db.session.add(User_test(username="Flask", email="example@example.com"))

users = User_test.query.all()

# # MySQL Connector using pymysql
# pymysql.install_as_MySQLdb()
#
# engine = create_engine("mysql+pymysql://root:hadoop@localhost/test_db", encoding='utf-8')
# conn = engine.connect()

@app.route('/')
def hello_world():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
