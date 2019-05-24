base:
	python setup.py install
dev: base
	pip install sphinx sphinx-rtd-theme pytest pytype
test: dev
	py.test tests
docs: dev
	python setup.py build_sphinx
package: test docs
	python setup.py sdist
check:
	pytype $(fpath)
proto:
	protoc -I. --python_out=okra/ protos/* ;\
	touch okra/protos/__init__.py
