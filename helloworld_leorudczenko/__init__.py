from pkg_resources import (
    get_distribution,
    DistributionNotFound,
)

from helloworld_leorudczenko.myscript import spacing
from helloworld_leorudczenko import extra
from helloworld_leorudczenko import testing


try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass
