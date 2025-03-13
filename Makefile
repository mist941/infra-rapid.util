test:
	pytest tests/

lint:
	flake8 src/

format:
	black src/ && isort src/