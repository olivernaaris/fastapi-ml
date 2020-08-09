#! /usr/bin/env bash

# Exit in case of error
set -e

ansible-playbook -i ../inventory/local ../delete.yml # Remove possibly previous broken stacks left hanging after an error

if [ $(uname -s) = "Linux" ]; then
    echo "Remove __pycache__ files"
    sudo find . -type d -name __pycache__ -exec rm -r {} \+
fi

ansible-playbook -i ../inventory/local ../build.yml
ansible-playbook -i ../inventory/local ../deploy.yml
POD=$(kubectl get pod -l app=fastapi-ml -o jsonpath="{.items[0].metadata.name}")
kubectl exec -ti "${POD}" -- bash /app/tests-start.sh

ansible-playbook -i ../inventory/local ../delete.yml