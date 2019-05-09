# Okra

[![image](https://travis-ci.org/okrahealth/okra.svg?branch=master)](https://travis-ci.com/)


Diagnose git health. 
=======
How healthy is our software? Okra is a tool that diagnoses the health of
projects which use git version control. Okra uses the 'bus factor' to
understand project health.

## What is the bus factor?

The bus factor is the smallest sized set of developers which own at least
50% of project files. Ownership of a file is determined by the author who
has contributed the most lines of code in a file.


## Getting Started

Git health can be related to an individual repo, organization, or
the dependencies within a repo.

## Setup and Installation (for development)

### Step 1: Configure pipenv

- Follow the instructions in the [pipenv README](https://github.com/pypa/pipenv/blob/master/README.md) to install pipenv on your system

### Step 2: Install dependencies

```shell
pipenv install
python setup.py install
```

### Step 3: Start pipenv shell

```shell
pipenv shell
```

This will spawn a new shell subprocess, which can be deactivated by using exit.

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

- [Okra Documentation](https://okrahealth.github.io/okra/)

