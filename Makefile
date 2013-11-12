.PHONY: clean test insert-data

all: clean test

test:
	nosetests lilkv/testsuite

clean:
	find . -name *.pyc -exec rm -fr {} +

insert-data:
