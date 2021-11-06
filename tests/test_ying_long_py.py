from ying_long_py import __version__
from ying_long_py.module import Mod
from ying_long_py.pin import Input, Output, Clock


def test_version():
    assert __version__ == '0.1.0'


class Mod1a(Mod):
    name = 'm114514'
    a = Input('in')
    b = Clock('in')

def test_work():

    ...
