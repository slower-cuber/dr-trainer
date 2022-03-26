.PHONY: local
local: venv/bin gen-twophase-tables
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

.PHONY: gen-twophase-tables
gen-twophase-tables:
	venv/bin/python -c 'import twophase.solver'

.PHONY: docker-build
docker-build: gen-twophase-tables
	docker build -t dr-trainer .
	docker save dr-trainer | gzip > dr-trainer.tgz

.PHONY: docker-run
docker-run:
	docker load < dr-trainer.tgz
	docker run -d -p 80:3033 --name dr_trainer dr-trainer
