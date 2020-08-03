#TODO
Make project run in Kubernetes
Add instruction to ReadMe

install docker python package
pip3 install docker openshift

# Create docker image using Ansible (takes a while). 
ansible-playbook -i inventory/local build.yml

# Deploy objects to Kubernetes cluster
ansible-playbook -i inventory/local deploy.yml

# Destroy objects to Kubernetes cluster
ansible-playbook -i inventory/local delete.yml

make sure you have at least 4GB assigned for your VM