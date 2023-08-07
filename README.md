# package-testing

> This is a simple library to provide terminal output spacing.

## Installation

```bash
pip install -i https://test.pypi.org/simple/ helloworld-leorudczenko
```

[PyPI Test Package](https://test.pypi.org/project/helloworld-leorudczenko/)

## Documentation

### spacing

Print a given number of empty lines. Default = 1.

## Usage

```python
from helloworld_leorudczenko import spacing

spacing(lines=2)
```

The `helloworld_leorudczenko` directory can be called directly. This will run the `spacing` function where `lines=3`.

## Development

### Dependencies

The dependencies can be found in the [pyproject.toml](https://github.com/leorudczenko/package-testing/blob/main/pyproject.toml) file.

### Package Distribution

To upload a distribution of the library run:

```bash
twine upload -r testpypi dist/*
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
