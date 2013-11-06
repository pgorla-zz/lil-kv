.PHONY: clean test insert-data

all: clean test

test:
	nosetests

clean:
	find . -name *.pyc -exec rm -fr {} +

insert-data:
