# Redis docker installation

Start standalone version of redis with:

```
docker run -p 6379:6379 redis
```

This docker does not have any storage volume attached to it so when stopped all the data will be lost. 

Please see the Apache Pulsar Documentation for proper installation.