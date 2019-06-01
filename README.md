# Okra

[![image](https://travis-ci.org/okrahealth/okra.svg?branch=master)](https://travis-ci.com/)
[![image](https://img.shields.io/pypi/l/okra.svg)](https://pypi.org/project/okra/)
[![image](https://img.shields.io/pypi/pyversions/okra.svg)](https://pypi.org/project/okra/)

## Diagnose git health. 

How healthy is our software? Okra is a tool that diagnoses the health of
projects which use git version control. Okra uses the 'bus factor' to
understand project health.

### What is the bus factor?

The bus factor is the smallest sized set of developers which own at least 
50% of project files. Ownership of a file is determined by the author who
has contributed the most lines of code in a file.

## Setup and Installation (for development)

We use [GNU make](https://www.gnu.org/software/make/manual/make.html#Introduction) to 
organize our build. It allows us to break our our package and development dependencies.
It also allows us to automate common tasks like running tests or building documentation.

### Step 1: Install and Configure a virtual environment

The recommended virtual environment for a statistical package is [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Once you have correctly installed
Miniconda, you can create an environment for Okra by executing the following commands
in your terminal

```
$ conda create -n myenv python=3.6
$ conda activate myenv
```

You can call `myenv` whatever is memorable for you. I've been using `ok` for mine.

### Step 2: Configuring your Development environment

Assuming that your virtual environment is activated, clone the Okra
repository and install the required development dependencies:

```
$ git clone https://github.com/okrahealth/okra.git
$ cd okra
$ make dev
```

### Step 3: Validate your development environment by getting tests passing

Assuming successful completion of steps (1) and (2), there should be no issue
getting tests passing.

```
$ make test
```

You should see a message similar to

```
...
========================== 27 passed, 2 warnings in 0.45 seconds ===========================
```

If tests are not passing for some reason, please open a ticket using
GitHub issues [okrahealth/okra/issues](https://github.com/okrahealth/okra/issues). 
You can also request membership to our slack channel, [https://okrahealth.slack.com](https://okrahealth.slack.com).

### Static Type Checking

We use a static type analyzer, [google/pytype](https://github.com/google/pytype),
to catch preventable bugs before they come out at runtime:

* Lint plain Python code, flagging common mistakes such as mispelled attribute names,
  incorrect function calls, and [many other errors](https://github.com/google/pytype/blob/master/docs/errors.md), even across file boundaries.
* Enforce user-provided [type annotations](https://www.python.org/dev/peps/pep-0484/). 
  While annotations are optional for pytype, it will check and apply them where 
  present.
  
More information can be found in the [pytype user guide](https://github.com/google/pytype/blob/master/docs/user_guide.md) or [pytype FAQ](https://github.com/google/pytype/blob/master/docs/faq.md). We use static type checking in Okra via the makefile:

```
$ make fpath=okra/be_nice.py check
```

where `okra/be_nice.py` can be any relative filepath that you've been
developing.

### Protocol Buffers

We use protocol buffers to define an interface between this package and the 
other Okra projects like [okrahealth/okra-api](https://github.com/okrahealth/okra-api). If new to protocol buffers, review [developers.google.com/protocol-buffers](https://developers.google.com/protocol-buffers/). Make sure you
have the [protocol buffer compiler](https://github.com/protocolbuffers/protobuf) installed. Protobuf files can be generated for the Okra Python
package:

```
$ make proto
```

Please contact a core developer before making any changes to the
`*.proto` files in `okra/protos/`.

## Documentation

- [Okra Documentation](https://okrahealth.github.io/okra/)
- [OkraHealth Website](https://okrahealth.github.io/)

## Usage

This statistical library is currently being used to compute batch jobs to populate
the database in [github.com/okrahealth/okra-api](https://github.com/okrahealth/okra-api).
We are not supporting other use cases at this time.
