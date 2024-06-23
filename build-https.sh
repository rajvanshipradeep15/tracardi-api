docker build . --rm --no-cache -f docker.ssl.Dockerfile -t tracardi/tracardi-api-ssl:0.9.0
docker push tracardi/tracardi-api-ssl:0.9.0