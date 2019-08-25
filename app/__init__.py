from flask import Flask
from flask_restful import Api
from controller import Keys, Key
from flask_prometheus import monitor


my_app = Flask(__name__)
monitor(my_app)

api = Api(my_app)
api.add_resource(Keys, '/keys')
api.add_resource(Key, '/keys/<string:key>')
