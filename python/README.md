# Python app

## Docker compose

To run the application and view it at http://localhost:5000
```
docker compose --file ./python/compose.yaml up --build -d
```

And to terminate it
```
docker compose --file ./python/compose.yaml down
```

To automatically update services in case of app updates
```
docker compose watch
```

## Kubernetes

To run the application and view it at http://localhost:30001
```
kubectl apply -f ./python/kubernetes.yaml
```

And to terminate it
```
kubectl delete -f ./python/kubernetes.yaml
```
