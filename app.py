import datetime
import json

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from flask_swagger import swagger
from pytz import timezone

from flask_restplus import Api, Resource

flask_app  = Flask(__name__)
app = Api(app = flask_app)

flask_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/test_db"
db = SQLAlchemy(flask_app, session_options={'autocommit': True})
name_space = app.namespace('main', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}

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

@flask_app.route('/')
def hello_world():
    return ""

@flask_app.route("/spec")
def spec():
    swag = swagger(flask_app)
    swag['info']['version'] = "2.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

if __name__ == '__main__':
    flask_app.run(debug=True)
