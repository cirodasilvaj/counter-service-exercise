# Counter Service

Simple Flask counter app for DevOps / Kubernetes practice.

## Structure

```
.
├── app.py              # Flask app: GET / increments and returns counter, /reset zeroes it, /health for probes
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   └── service.yaml
└── references/
    └── README_addition.md
```

## Run locally

```bash
pip install flask
python app.py
curl http://localhost:5000/
```

## Run with Docker

```bash
docker compose up --build
curl http://localhost:5000/
```

## Deploy to your EKS cluster (kube-demo-eks)

Cluster: kube-demo-eks | Region: us-east-1 | Account: 767397779454

```bash
aws eks update-kubeconfig --region us-east-1 --name kube-demo-eks --account-id 767397779454
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -n counter-service
kubectl get svc -n counter-service
```

Get LoadBalancer URL and test:

```bash
export LB_URL=$(kubectl get svc counter-service -n counter-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
echo "LB URL: $LB_URL"
curl http://$LB_URL/
```

Repo: https://github.com/cirobessa/kube-demo-2026
Original article: https://medium.com/devops-technical-notes-and-manuals/devops-example-project-for-your-resume-198e34d874b4
