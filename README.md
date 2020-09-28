# python-cli-template

A starting point for building Python Command Line Applications.

## About 

This project serves as a starting point to developing command line modules with Python. It is structured in such a way that 
when we call the module it executes the main method in `app/cli.py`. This is typically where you would want to add 
your own logic.

The setup.py file includes some advanced patterns and best 
practices for setup.py, as well as some commented–out nice–to–haves. For example, it provides a `python 
setup.py upload` command, which creates a universal wheel (and sdist) and uploads your package to PyPi using Twine. 
It also creates/uploads a new git tag, automatically.

## Setup

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python -m app --help
```

## Packaging 

Update `setup.py` with your details and then run `python setup.py upload` to package for distribution on PyPi.

## Contributing

- Fork the project and clone locally.
- Create a new branch for what you're going to work on.
- Push to your origin repository.
- Create a new pull request in GitHub.
