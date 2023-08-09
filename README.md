# package-testing

> This is a simple library to provide terminal output spacing.

## Installation

**Because this test package is using PyPI test for distribution, installation requries the `--extra-index` flag to include real up-to-date packages in dependencies.**

Standard library installation:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index https://pypi.org/simple helloworld-leorudczenko
```

Development library installation:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index https://pypi.org/simple helloworld-leorudczenko[dev]
```

[PyPI Test Package](https://test.pypi.org/project/helloworld-leorudczenko/)

## Documentation

### spacing

Print a given number of empty lines. Default = 1.

#### Usage

Python scripting:

```python
from helloworld_leorudczenko import spacing

spacing(lines=2)
```

Command Line Interface:


- Once the package has been installed, `leorud-spacing` will run the `spacing` function where `lines=3`.
- The `helloworld_leorudczenko` directory can be called directly. This will run the `spacing` function where `lines=3`.

### hash_spacing

Print a given number of hash lines. Default = 1.

```python
from helloworld_leorudczenko.extra import hash_spacing

hash_spacing(lines=2)
```

## Development

### Dependencies

The dependencies can be found in the [pyproject.toml](https://github.com/leorudczenko/package-testing/blob/main/pyproject.toml) file.

### Package Distribution

First, you will need to create a new git release. You should only do this after all commits for the release have been made.

**Once you have created a new release, ensure you pull the newest tag matching that release locally before building local distributions.** _This is because `setuptools_scm` uses the latest git tag versioning to update the dynamic version in the `pyproject.toml` config file during the build._

Then, you need to build the distribution files:

```bash
python -m build
```

Then you can upload the distribution of the library to PyPI test:

```bash
twine upload -r testpypi dist/*
```

If you encouter the error `File already exists`, this is because you have likely an older version locally in your `dist/` directory. To work around this, run:

```bash
twine upload --skip-existing -r testpypi dist/*
```

You will then be prompted to login with your username and password. Alternatively, you can authenticate using an API token:

```bash
Enter your username: __token__
Enter your password: ******
```

**Note:** _When using an API token, your username should be `__token__` and your password should be your API token._

## Helpful Links
- [Packaging Your Python Code With pyproject.toml | Complete Code Conversation](https://www.youtube.com/watch?v=v6tALyc4C10)
- [Official Python Packaging Documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [RealPython TOML Files](https://realpython.com/python-toml/)
- [RealPython PyPI Publishing](https://realpython.com/pypi-publish-python-package/)
- [Great Introduction to Python Packaging](https://www.youtube.com/watch?v=5KEObONUkik)
- [Python Packaging Live Talk](https://www.youtube.com/watch?v=GIF3LaRqgXo)
- [Good PyPI Test Demonstration](https://www.youtube.com/watch?v=JkeNVaiUq_c)
- [Versioning with setuptools_scm](https://www.moritzkoerber.com/posts/versioning-with-setuptools_scm/)
- [setuptools - Package Discovery](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#finding-simple-packages)
- [pyproject.toml and the cmdclass](https://github.com/pypa/packaging-problems/issues/657)
- [PyPI Test --extra-index](https://github.com/numpy/numpy/issues/21281)
