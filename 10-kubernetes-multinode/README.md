# Exercise 10: Multi-Node Kubernetes Cluster

## Objective
Deploy two applications on a three-node Minikube Kubernetes cluster with replicas distributed across nodes.

## Applications

### Product Catalog
- Deployment: product-catalog
- Replicas: 2
- Endpoint: GET /products
- Returns Laptop, Phone, and Headphones.
- Service: product-catalog-service

### Shopping Cart
- Deployment: shopping-cart
- Replicas: 3
- Endpoints: GET /cart and POST /cart
- Supports viewing the cart and adding an item.
- Service: shopping-cart-service

## Technology Stack
- Docker
- Python and Flask
- Kubernetes
- Minikube
- Windows 11 PowerShell

## Cluster
Minikube profile: devops-multinode

Nodes:
- devops-multinode (control plane)
- devops-multinode-m02 (worker)
- devops-multinode-m03 (worker)

## Deployment and Availability
Both Deployments use required pod anti-affinity with topology key kubernetes.io/hostname.

- Product Catalog: 2/2 replicas running on separate worker nodes.
- Shopping Cart: 3/3 replicas running across all three nodes.
- Both Services are NodePort Services in the default namespace.
- Both Services have endpoints connected to their application pods.

## Docker Images
- product-catalog:latest
- shopping-cart:latest

## Verification
- All three Kubernetes nodes are Ready.
- Product Catalog returns three products through /products.
- Shopping Cart returns an empty list through GET /cart initially.
- A POST request successfully added a Laptop with quantity 1.

## Important Note
The Shopping Cart stores items in application memory. Data is not shared between replicas and may be lost when a pod restarts. Persistent, shared storage is outside the scope of this exercise.

## Evidence
Screenshots of successful application tests are stored in the evidence/ directory.
