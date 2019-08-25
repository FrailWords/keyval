### Pre-requisites for running/testing the application

* Python 3.7 
* Pipenv
* Docker
* Docker Compose

### Running the application

Run the application by executing the shell script `./run.sh`.

### Running the tests

Run the tests using the command `pipenv run pytest`

Application should be available at `http://localhost:5000` 

### Application Design

The application is built using `Flask RESTful` as the base http framework, with `redis` as a file-backed cache/storage.

### Testing Design

For testing, `pytest` is used along-side `fakeredis` for running a fake redis instance for the test and using fixtures for the Flask client.

### Testing Strategy

In this submission, the tests are located in the file `test_controller`.  They are unit testing the http endpoints with 'sociable' check against the fake redis storage.
These are somewhere between a unit test and an integration test, tending more towards integration test.

### Monitoring

The application is connected to Prometheus using the `Flask Prometheus` exporter that automatically exports metrics that are Flask specific.
Grafana comes up on port `3000` with username/password as default of `admin:admin` and is already connected to the datasource coming from the application on port `8000`.
In terms of dashboards, there aren't any that are part of this submission as I created a couple using the Flask metrics but they didn't persist.


### Code Structure
Being not so familiar with Python, the code structure is what worked for me and it could probably be better.
