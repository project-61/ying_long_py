from typing import Optional, overload
from ying_long_py import __version__
from ying_long_py.datatype import *
from ying_long_py.modules import *


def test_version():
    assert __version__ == '0.1.0'


@yl
class Mod114(Module):
    class io:
        i = Int(32)
        o = Int(32)
    io.o <= io.i

