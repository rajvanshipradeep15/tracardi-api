docker build . --rm --no-cache -f Dockerfile.ssl -t tracardi/tracardi-api-ssl:0.7.4-dev
docker push tracardi/tracardi-api-ssl:0.7.4-dev