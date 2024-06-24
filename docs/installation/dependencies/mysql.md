# MySql docker installation

Start standalone version of mysql with root password set to `root`:

```
docker run -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql
```

This docker does not have any storage volume attached to it so when stopped all the data will be lost. 

Please see the MySql Documentation for proper installation.