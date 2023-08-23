install:
	export PYTHONPATH=./src
	pip install .

clean:
	rm -rf build dist *.egg-info
	rm -rf .pytest_cache
	rm -rf src/agents.egg-info
	python setup.py clean

test:
	pytest -v
	pytest test --cov-report=html