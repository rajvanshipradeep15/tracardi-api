# Workers Installation

Tracardi relies on four different workers to ensure smooth operations and efficient processing of data. Each worker
serves a specific purpose in the Tracardi ecosystem. Below are details about each worker and instructions on how to set
them up.

## Open-source workers

### 1. Migration and Update Worker

The Migration and Update Worker is responsible for system upgrades and data import tasks, which are carried out in the
background. It ensures a seamless transition when updating the Tracardi system and handles data imports efficiently.

To run the Migration and Update Worker, execute the following Docker command:

```bash
docker run \
-e ELASTIC_HOST=http://<elasitc-ip>:9200 \
-e REDIS_HOST=redis://<redis-ip>:6379 \
-e MYSQL_HOST=<mysql-ip> \
tracardi/update-worker:0.9.0
```

Please ensure that you replace `<...-ip>` with the actual IP address of your service instance.


### 2. Automatic Profile Merging Worker (APM)

The APM Worker is responsible for auto merging profiles with the same emails.

To run the APM Worker, execute the following Docker command:

```bash
docker run \
-e ELASTIC_HOST=http://<elasitc-ip>:9200 \
-e REDIS_HOST=redis://<redis-ip>:6379 \
-e MYSQL_HOST=<mysql-ip> \
-e MODE=worker \
-e PAUSE=5 \
tracardi/apm:0.9.0.4
```

Please ensure that you replace `<...-ip>` with the actual IP address of your service instance.

## Commercial workers

In order to install commercial version you will need to log-in to docker hub with our credentials.

```
docker login -u tracardi -p <token>
```

And paste the credentials that we have sent you.

## Set up License Key

Then create a file .env-docker and paste the LICENSE in it:

```
API_LICENSE="paste license here"
```

When running linux:

```
set -a
source .env-docker
```

### 1. Init script

Before you run any commercial docker please make sure that all dependencies are running and you start init script:

```bash
docker run \
-e LICENSE=xxx \
-e ELASTIC_HOST=http://<elastic-ip>:9200 \
-e REDIS_HOST=redis://<redis-ip>:6379 \
-e MYSQL_HOST=<mysql-ip> \
-e PULSAR_HOST=pulsar://<pulsar-ip>:6650 \
-e PULSAR_API=http://<pulsar-ip>:8080 \
-e LOGGING_LEVEL=info \
tracardi/init:0.9.0.4
```

### 2. Tenant Management System (TMS)

The Tenant Management System (TMS) is a dedicated microservice responsible for managing various aspects related to tenants within a system or platform, particularly in a multi-tenant environment. I

To run this worker, execute the following Docker command:

```bash
docker run -p 8081:80 \
-e API_KEY=<random-api-key> \
-e SECRET=<random-secret> \
-e MYSQL_HOST=<mysql-ip> \
tracardi/tms:0.9.0.4
```

Set <random-api-key> and <random-secret> to random values.

### 3. Background Worker

The Background Worker is a commercial worker responsible for processing background jobs. 

To run the Background Worker, execute the following Docker command:

```bash
docker run \
-e LICENSE=xxx \
-e ELASTIC_HOST=http://<elastic-ip>:9200 \
-e REDIS_HOST=redis://<redis-ip>:6379 \
-e MYSQL_HOST=<mysql-ip> \
-e PULSAR_HOST=pulsar://<pulsar-ip>:6650 \
-e PULSAR_API=http://<pulsar-ip>:8080 \
-e LOGGING_LEVEL=info \
tracardi/background-worker:0.9.0.4
```

