from typing import Optional, overload
from ying_long_py import __version__
from ying_long_py.module import Always, Mod, Negedge, Posedge
from ying_long_py.pin import Input, Output, Clock


def test_version():
    assert __version__ == '0.1.0'


class Mod1a(Mod):
    name = 'm114514'
    clk = Clock()
    a = Input('in')

    def always(self, a: Posedge) -> Optional[Always]:
        ...

def test_work():

    ...
