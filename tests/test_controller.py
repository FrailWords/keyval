import unittest
import pytest
import testing.redis
from flask import url_for
import mock
import os
from db import db
import json


@pytest.mark.usefixtures('client_class')
@mock.patch.dict(os.environ, {"REDIS_HOST": "127.0.0.1"})
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.redis = testing.redis.RedisServer(port=6379)

    def test_key_by_id(self):
        db.set("key1", "value")
        response = self.client.get("/keys/key1")
        assert response.status_code == 200
        assert response.json == "value"

    def test_key_by_id_does_not_exist(self):
        response = self.client.get("/keys/key1")
        assert response.status_code == 404

    def test_key_exists(self):
        db.set("key1", "value")
        response = self.client.head("/keys/key1")
        assert response.status_code == 200

    def test_key_does_not_exist(self):
        response = self.client.head("/keys/key1")
        assert response.status_code == 404

    def test_key_delete(self):
        db.set("key1", "value")
        response = self.client.delete("/keys/key1")
        assert response.status_code == 200
        assert db.get("key1") is None

    def test_key_delete_does_not_exist(self):
        response = self.client.delete("/keys/key1")
        assert response.status_code == 404

    def test_keys_get(self):
        db.set("key1", "value1")
        db.set("key2", "value2")
        response = self.client.get(url_for('keys'))
        assert response.status_code == 200
        response_json = json.loads(response.json)
        assert response_json['key1'] == "value1"
        assert response_json['key2'] == "value2"

    def test_keys_delete(self):
        db.set("key1", "value1")
        db.set("key2", "value2")
        response = self.client.delete(url_for('keys'))
        assert response.status_code == 200
        assert len(db.keys("*")) is 0

    def test_key_insert(self):
        self.client.put('/keys', json={'id': 'key1', 'value': 'value1'})
        assert db.get("key1") == "value1"
        assert db.ttl("key1") == -1

    def test_key_update(self):
        db.set('key1', 'value1')
        self.client.put('/keys', json={'id': 'key1', 'value': 'value2'})
        assert db.get("key1") == "value2"

    def test_key_insert_with_expires(self):
        self.client.put('/keys?expire_in=60', json={'id': 'key1', 'value': 'value1'})
        assert db.get("key1") == "value1"
        assert db.ttl("key1") == 60

    def tearDown(self):
        self.redis.stop()


if __name__ == '__main__':
    unittest.main()
