# Counter Service

A minimal Flask counter app for Kubernetes practice.

## Run

```bash
pip install flask
python app.py
```

## Deploy

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
