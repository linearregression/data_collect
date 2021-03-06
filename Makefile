# -*- mode: Makefile; fill-column: 80; comment-column: 75; -*-
PYC_DIR = .

get-tag:
	./get_version.sh

get-deps:
	pip install flask boto six

clean_pyc:
	find $(PYC_DIR) -type f -name "*.pyc" -delete
	rm -f *.log
 
run:
	python api.py


all: clean_pyc get-deps get-tag run
 
