# fastapi-ml

## Operational Requirements
* [Docker](https://www.docker.com/).
* [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

### Install Operational Python dependencies
```console
$ poetry install
```

## Backend local development

* Create docker image using Ansible (takes a while). 

```bash
ansible-playbook -i inventory/local build.yml
```

* Start the stack with Ansible (running on Kubernetes):

```bash
ansible-playbook -i inventory/local deploy.yml
```

* Terminate the stack with Ansible (running on Kubernetes):

```bash
ansible-playbook -i inventory/local delete.yml
```

Backend, JSON based web API based on OpenAPI: http://localhost:8000/api/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost:8000/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost:8000/redoc

To check the logs of a specific service, add the name of the service, e.g.:

```bash
kubectl logs -l tier=backend -f
```

## Backend local development, additional details

### General workflow

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

From `./backend/app/` you can install all the dependencies with:

```console
$ poetry install
```

Then you can start a shell session with the new environment with:

```console
$ poetry shell
```

Next, open your editor at `./backend/app/` (instead of the project root: `./`), so that you see an `./app/` directory with your code inside. That way, your editor will be able to find all the imports, etc. Make sure your editor uses the environment you just created with Poetry.

Modify or add SQLAlchemy models in `./backend/app/app/models/`, Pydantic schemas in `./backend/app/app/schemas/`, API endpoints in `./backend/app/app/api/`, CRUD (Create, Read, Update, Delete) utils in `./backend/app/app/crud/`. The easiest might be to copy the ones for Items (models, endpoints, and CRUD utils) and update them to your needs.

Add and modify tasks to the Celery worker in `./backend/app/app/worker.py`.

If you need to install any additional package to the worker, add it to the file `./backend/app/celeryworker

### Backend tests

To test the backend run:

```console
$ sh ./scripts/test.sh
```

The file `./scripts/test.sh` has the commands to trigger tests inside the container.

The tests run with Pytest, modify and add tests to `./backend/app/app/tests/`.