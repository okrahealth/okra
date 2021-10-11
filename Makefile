base:
	python setup.py install
dev: base
	pip install sphinx sphinx-rtd-theme pytest mypy
test: dev
	pytest tests
docs: dev
	python setup.py build_sphinx
check:
	mypy okra
package: docs test check
	python setup.py sdist
proto: 
	protoc -I. --python_out=okra/ proto/* ;\
	touch okra/proto/__init__.py
