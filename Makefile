base:
	python setup.py install
dev: base
	pip install sphinx sphinx-rtd-theme pytest pytype nbformat
test: dev
	py.test tests
docs: dev
	python setup.py build_sphinx
check:
	pytype $(fpath)
package: docs test check
	python setup.py sdist
proto: 
	protoc -I. --python_out=okra/ proto/* ;\
	touch okra/proto/__init__.py
