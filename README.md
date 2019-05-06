# Okra

Diagnose git health. 

## Getting Started

Git health can be related to an individual repo, organization, or
the dependencies within a repo. 

### Install

```shell
python setup.py install
```

### Diagnose Health for a git repo

```
from okra.playbooks import truck_factor
truck_factor(repo_name)
```

### Diagnose Health of an Organization on GitHub

clone all their repos, generate a bus schedule

### Diagnose Health of dependencies in git repo

find all dependencies, clone all their repos, generate a bus schedule

## Tests

```shell
python setup.py test
```

## Documentation

Generate documentation

```shell
python setup.py build_sphinx
```

## View documentation

Need to deploy docs to github pages

