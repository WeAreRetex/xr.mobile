#!/bin/bash

# Configura il contesto kubectl
export KUBECONFIG=$(pwd)/.k8s/kubeconfig.yaml

# Applica la configurazione Kubernetes
kubectl apply -k .k8s/

# Verifica lo stato del deployment
echo "Verificando lo stato del deployment..."
kubectl rollout status deployment/xr-mobile-api -n xr-bo-mobile

echo "Deployment completato!"
echo "L'API sarà disponibile all'indirizzo: https://xr-mobile-api.crfs-platform-alba.k.retexcloud.io"
