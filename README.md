# Okra

[![image](https://travis-ci.org/okrahealth/okra.svg?branch=master)](https://travis-ci.com/)
[![image](https://img.shields.io/pypi/l/okra.svg)](https://pypi.org/project/okra/)
[![image](https://img.shields.io/pypi/pyversions/okra.svg)](https://pypi.org/project/okra/)

## Diagnose git health. 

How healthy is our software? Okra is a tool that diagnoses the health of
projects which use git version control. Okra uses analytics, not buzzwords,
create a Jupyter notebook report on the health of a specific project.

The pre-alpha version of Okra is a command line tool:

```
$ okra --help
$ okra upsert JuliaLang IJulia.jl "sqlite:///ijulia.db" "JuliaLang/IJulia.jl" "https://github.com/JuliaLang/IJulia.jl.git" 
```

This command will clone/fetch updates from a repo and persist log information within a sqlite database. In this example,
we're cloning `IJulia.jl`, and populating a sqlite database `ijulia.db`.

## Documentation

- [Okra Documentation](https://okrahealth.github.io/okra/)
- [OkraHealth Website](https://okrahealth.github.io/)

## File an Issue

GitHub issues [okrahealth/okra/issues](https://github.com/okrahealth/okra/issues). 
You can also request membership to our slack channel, [https://okrahealth.slack.com](https://okrahealth.slack.com).

## Contributing

Assuming that your virtual environment is activated, clone the Okra
repository and install the required development dependencies:

```
$ git clone --recurse-submodules https://github.com/okrahealth/okra.git
$ cd okra
```

Okra uses a submodule, [tbonza/tiny_dancer](https://github.com/tbonza/tiny_dancer), for 
testing purposes. Make sure you initialize the submodule after cloning Okra so that your
tests will be passing.

Validate the clone and master branch by ensuring that tests are passing.

```
$ make test
```

Please [open an Okra issue](https://github.com/okrahealth/okra/issues) if your tests aren't
passing.
