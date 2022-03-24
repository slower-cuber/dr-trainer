.PHONY: local
local: venv/bin
	venv/bin/uvicorn src.main:app --port 3033 --reload

venv:
	python -m venv venv
	venv/bin/pip install --upgrade pip

src/requirements.txt: src/requirements-to-freeze.txt
	venv/bin/pip install -r src/requirements-to-freeze.txt --upgrade
	venv/bin/pip freeze > src/requirements.txt

venv/bin: venv src/requirements.txt
	venv/bin/pip install -r src/requirements.txt

.PHONY: upgrade
upgrade: venv src/requirements-to-freeze.txt
	venv/bin/pip install -r src/requirements-to-freeze.txt --upgrade
	venv/bin/pip freeze > src/requirements.txt

.PHONY: docker-build
docker-build:
	docker build -t dr-trainer .

.PHONY: docker-run
docker-run:
	docker run -d -p 55666:3033 --name dr_trainer dr-trainer
