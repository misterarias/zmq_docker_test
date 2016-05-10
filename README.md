# Fun with Docker and Zero-MQ

You can start things up slowly

```bash
    docker-compose up
```

Or you can shake it up a little

```bash
docker-compose up -d pub_server
docker-compose scale pub_client=10
```

From here onwards... anything can happen
