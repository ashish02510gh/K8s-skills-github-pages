Containerizing the K8s Skills Flask App

This file explains how to build and run the provided Docker image and an example Kubernetes manifest.

Build & Run with Docker
-----------------------

Build the image locally:

```powershell
docker build -t k8s-skills-web:latest .
```

Run the container (production-like):

```powershell
docker run --rm -p 8000:8000 \
  -e SECRET_KEY="your-secure-secret" \
  --name k8s_skills_web k8s-skills-web:latest
```

Or run using `docker-compose`:

```powershell
docker-compose up -d --build
docker-compose logs -f
```

Environment variables
---------------------
- `SECRET_KEY` - set a long random string in production.
- `FLASK_ENV` - set to `production` for production container.

Push to a registry (Docker Hub example)
---------------------------------------

```powershell
docker tag k8s-skills-web:latest <your-dockerhub-username>/k8s-skills-web:latest
docker push <your-dockerhub-username>/k8s-skills-web:latest
```

Kubernetes Manifests (Quickstart)
---------------------------------
Create the following manifests and apply with `kubectl apply -f k8s/` (scaffolds created in repo):
- `k8s/deployment.yaml`
- `k8s/service.yaml`

Secrets & Config
----------------
Store `SECRET_KEY` and other sensitive values in Kubernetes Secrets or your cloud provider's secrets store (Azure Key Vault, AWS Secrets Manager).

Ingress / TLS
-------------
Use an Ingress controller (nginx/traefik) to terminate TLS and route traffic to the service.

Next steps
----------
- I can scaffold a Helm chart to parameterize image name, replicas, resources, and ingress.
- I can add an Nginx sidecar to serve static assets if you want more control over caching headers.
