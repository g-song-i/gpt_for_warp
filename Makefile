.PHONY: install requirements run

default: run

install:
	pip3 install -r requirements.txt

requirements:
	pip3 freeze > requirements.txt

run:
	python3 main.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

setup:
	cp config_template.ini .config.ini
	echo "Please update .config.ini with your actual configuration settings."
