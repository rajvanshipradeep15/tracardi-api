## Dependencies Installation with helm chart scripts

Tracardi dependencies can be installed using installation scripts. Provided script may need changes for proper scaling.

## Prerequisites

* kubectl 1.21 or higher, compatible with your cluster (+/- 1 minor release from your cluster)
* Helm v3 (3.10.0 or higher)
* A Kubernetes cluster, version 1.21 or higher.
* Access to tracardi scripts repo. This is where the scripts are stored.

## Install Dependencies Using Helm Scripts

Tracardi depends on:

- Elasticsearch
- Apache Pulsar
- Redis
- Mysql (Percona)

### Install Elasticsearch

```
cd argocd
bash ./elastic-install-operator.sh
bash ./elastic-install-helm.sh
```

To customize installation values go to: elastic/local-values.yaml

### Install Apache Pulsar

```
cd argocd
bash ./pulsar-install-helm.sh
```

To customize installation values go to: pulsar/local-values.yaml

### Install Redis

```
cd argocd
bash ./redis-install-repo.sh
bash ./redis-install-helm.sh
```

To customize installation values go to: redis/local-values.yaml

### Install Percona

```
cd argocd
bash ./percona-install-repo.sh
bash ./percona-install-helm.sh
```

To customize installation values go to: percona/local-values.yaml
