from flask import Flask
from flask_restful import Api
from controller import Keys, Key
from flask_prometheus import monitor


app = Flask(__name__)
monitor(app)

api = Api(app)
api.add_resource(Keys, '/keys')
api.add_resource(Key, '/keys/<string:key>')


def main(*args):
    app.run(host="web", debug=False)


if __name__ == "__main__":
    main()
