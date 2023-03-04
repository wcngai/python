install:
	pip install upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black .

lint:
	pylint --disable=R,C --ignore-patterns=test_*.py .

all:
	install lint test
	