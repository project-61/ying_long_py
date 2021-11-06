

from typing import Any, Dict, List

from ying_long_py.gen_id import gen_id


class Pin:
    name: str
    in_: Any
    out_: Any
    def __init__(self, name: str = gen_id()) -> None:
        self.name = name


class Clock(Pin):
    def __init__(self, name: str = gen_id()) -> None:
        super().__init__(name=name)


class Bundle(Pin):
    name: str
    values: List[Pin]
    def __init__(self, name: str = gen_id(), *args: Pin):
        self.name = name
        self.values = list(args)
    def get(self, i: int) -> Pin:
        return self.values[i]
    def get_range(self, l: int, r: int) -> List[Pin]:
        return self.values[l:r]


class PinMap:
    map: Dict[str, Pin]
    def __init__(self, *args) -> None:
        self.map = {arg: Pin() for arg in args}
    def __getattribute__(self, name: str) -> Pin:
        return self.map[name]


class Input(PinMap):
    pass

class Output(PinMap):
    pass