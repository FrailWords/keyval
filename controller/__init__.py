from flask_restful import Resource
from flask_restful import request, abort
from db import db
import json


class Key(Resource):
    def get(self, key):
        exists = db.exists(key)
        if exists:
            return str(db.get(key)), 200
        else:
            return abort(404, message="Key not found.")

    def head(self, key):
        exists = db.exists(key)
        if exists:
            return "Key exists.", 200
        else:
            return abort(404, message="Key not found.")

    def delete(self, key):
        exists = db.exists(key)
        if exists:
            db.delete(key)
            return "Key deleted.", 200
        else:
            return abort(404, message="Key not found.")


class Keys(Resource):
    def put(self):
        data = request.json
        if 'id' not in data or 'value' not in data:
            return abort(400, message="Required fields 'id' and 'value'.")
        key = data['id']
        value = data['value']
        args = request.args
        if args:
            expire_in = args['expire_in']
            if expire_in:
                db.set(key, value, ex=int(expire_in))
        else:
            db.set(key, value)
        return "Successfully updated.", 200

    def get(self):
        pattern = "*"
        args = request.args
        if args:
            filter_wildcard = args['filter']
            if filter_wildcard:
                pattern = filter_wildcard
        json_data = {}
        keys = db.keys(pattern=pattern)
        for key in keys:
            json_data[key] = str(db.get(key))
        return json.dumps(json_data), 200

    def delete(self):
        db.flushall(asynchronous=True)
        return "Successfully cleared database.", 200
