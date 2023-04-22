install:
    pip install -r requirements.txt

run:
    flask run --port=5000 --app=server.src.application.app:create_app()

test:
    pytest

clean:
    rm -rf __pycache__/
