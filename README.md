# Counter Service

A minimal Flask counter service for DevOps / Kubernetes practice.

## Endpoint

- `GET /count` — increments and returns the current count as JSON.

## Run locally

```bash
pip install flask
python app.py
curl http://localhost:5000/count
```

## Deploy to Kubernetes

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
