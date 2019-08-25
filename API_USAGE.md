## API Usage Examples

### Insert a key value
`curl -X PUT http://localhost:5000/keys?expire_in=100  --header 'content-type: application/json' --data "{\"id\": \"key1\", \"value\": \"value1\"}"`

### Get value for key
`curl http://localhost:5000/keys/key1`

### Delete key
`curl -X DELETE http://localhost:5000/keys/key1`

### Get all values
`curl http://localhost:5000/keys`

### Get all values starting with 'test'
`curl http://localhost:5000/keys?filter=test*`

### Delete all values
`curl -X DELETE http://localhost:5000/keys`

### Delete all values
`curl -X DELETE http://localhost:5000/keys`


