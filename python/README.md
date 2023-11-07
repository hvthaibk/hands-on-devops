# Python app

To run the application and view it at http://localhost:5000
```
docker compose up --build -d
docker compose --file ./python/compose.yaml up --build -d
```

And to terminate it
```
docker compose down
docker compose --file ./python/compose.yaml down
```

To automatically update services in case of app updates
```
docker compose watch
```
