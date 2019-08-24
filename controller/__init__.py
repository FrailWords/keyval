from simple_http_server import request_map
from simple_http_server import JSONBody
from simple_http_server import PathValue
from simple_http_server import Response
from simple_http_server import Parameter
from db import db
import json


@request_map("/keys", method="PUT")
def update_value(data=JSONBody(), expire_in=Parameter("expire_in"), res=Response()):
    if 'id' not in data or 'value' not in data:
        return res.send_error(status_code=400)
    key = data['id']
    value = data['value']
    if expire_in:
        db.set(key, value, ex=int(expire_in))
    else:
        db.set(key, value)


@request_map("/keys", method="GET")
def get_all_key_values():
    keys = db.getall()
    json_data = json.dumps({})
    for key in keys:
        json_data[key] = str(db.get(key))
    return json_data


@request_map("/keys/{id}", method="GET")
def get_key_value(key=PathValue("id"), res=Response()):
    exists = db.exists(key)
    if exists:
        return str(db.get(key))
    else:
        return res.send_error(status_code=404)


@request_map("/keys/{id}", method="HEAD")
def key_exists(key=PathValue("id"), res=Response()):
    exists = db.exists(key)
    if exists:
        return res.send_response()
    else:
        return res.send_error(status_code=404)


@request_map("/keys/{id}", method="DELETE")
def delete_key(key=PathValue("id"), res=Response()):
    exists = db.exists(key)
    if exists:
        db.delete(key)
    else:
        return res.send_error(status_code=404)


@request_map("/keys", method="DELETE")
def delete_all_key_values():
    db.flushall(asynchronous=True)
