# To Use Kompose
- Ensure ```kompose``` is installed, otherwise brew install it or use other pkg installer tools suitable for your machine.
- Resolve env variable reference in docker compose
    ```
    docker-compose config > docker-compose-resolved.yaml
    ```
- Compile resolved docker compose file to k8s yamls.
    ```
    kompose convert -f docker-compose-resolved.yaml
    ```