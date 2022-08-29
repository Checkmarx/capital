# Pyarmor the backend
## Obfuscation

```sh
docker build -f DockerfilePyarmor . -t ctf-obfuscate
docker run --name obfuscated-api-ctf ctf-obfuscate
docker cp obfuscated-api-ctf:/app/dist .
docker rm obfuscated-api-ctf

docker build -f Dockerfile . -t api-ctf

Docker-compose up
```
