Since I am not so hands-on with Python, this submission took a while and I wanted to document my progress here.

Initially, I started with `PickleDB` and `simple-http-server` and wrote all the things but then I realized that a few  
requirements didn't work very well with that - testing, monitoring and the `expires` requirement.

Because of the `expires` requirement, I moved to `redis`.  Because of monitoring and testing, I moved to Flask as it 
seems to be one of more popular frameworks, with readily available examples and libraries.