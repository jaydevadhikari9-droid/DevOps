# Kubernetes Hands-On Exercise

## Overview
This project demonstrates deploying an Nginx web server on a local Kubernetes cluster using Minikube and Docker.

## Tools Used
- Docker Desktop
- Minikube
- Kubernetes (`kubectl`)
- Git and GitHub
- Windows PowerShell

## Project Structure
```text
kubernetes-hands-on/
├── README.md
├── k8s/
│   ├── pod.yaml
│   └── service.yaml
└── evidence/
    └── verification.txt
```

## Prerequisites
Install and configure Docker Desktop, Minikube, kubectl, and Git.

Ensure Docker Desktop is running before starting Minikube.

## Start the Kubernetes Cluster
```powershell
minikube start --driver=docker
```

Verify the cluster:
```powershell
kubectl get nodes
```

## Deploy the Application
Apply the Kubernetes manifests:
```powershell
kubectl apply -f k8s/
```

Wait for the Pod to become ready:
```powershell
kubectl wait --for=condition=Ready pod/hello-k8s --timeout=180s
```

## Verify the Deployment
```powershell
kubectl get pods
kubectl get services
kubectl describe pod hello-k8s
```

## Access the Nginx Web Server
Forward the service to your local computer:
```powershell
kubectl port-forward service/hello-k8s 8080:80
```

Open this URL in your browser:

http://localhost:8080

You should see the Nginx welcome page.

## Save Verification Evidence
Create the evidence folder if needed:
```powershell
New-Item -ItemType Directory -Force evidence
```

Save cluster and deployment information:
```powershell
kubectl get nodes | Out-File evidence/verification.txt
kubectl get pods -o wide | Out-File evidence/verification.txt -Append
kubectl get services -o wide | Out-File evidence/verification.txt -Append
kubectl describe pod hello-k8s | Out-File evidence/verification.txt -Append
```

## Cleanup
When finished, remove the deployed resources:
```powershell
kubectl delete -f k8s/
```

Stop Minikube:
```powershell
minikube stop
```

## Author
Created as a hands-on Kubernetes learning project.
