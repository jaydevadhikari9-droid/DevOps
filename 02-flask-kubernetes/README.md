
## Step 6 — Check Minikube and Docker

First check that Minikube is running:

```powershell
minikube status
kubectl get nodes
docker info --format '{{.OSType}}'