export FLASK_APP=src/application/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export PYTHONPATH=$(shell pwd)

install:
	pip install -r requirements.txt

run:
	flask run --port=5000 

test:
	pytest

clean:
	rm -rf __pycache__/
