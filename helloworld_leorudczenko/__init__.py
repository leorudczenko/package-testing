from importlib.metadata import (
    PackageNotFoundError,
    version,
)

from helloworld_leorudczenko.myscript import spacing
from helloworld_leorudczenko import extra
from helloworld_leorudczenko import testing


try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "0.0.0"
