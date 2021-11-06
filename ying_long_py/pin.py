from typing import Any, Dict, List, Optional, Tuple

from ying_long_py.gen_id import gen_id


class Pin:
    name: str
    in_: Any
    out_: Any

    def __init__(self, name: str = gen_id()) -> None:
        self.name = name

    def let(self, in_) -> 'Pin':
        self.in_=in_
        return in_

    def get(self, i: int) -> 'Pin':
        ...

    def get_range(self, l: int, r: int) -> List['Pin']:
        ...

    def __len__(self) -> int:
        return 1

    def __or__(self, other: 'Pin') -> 'Pin':
        return Pin().let(Or(self, other))
    def __xor__(self, other: 'Pin') -> 'Pin':
        return Pin().let(Xor(self, other))
    def __and__(self, other: 'Pin') -> 'Pin':
        return Pin().let(And(self, other))
    def __add__(self, other: 'Pin') -> 'Pin':
        return Pin().let(Add(self, other))
    def __invert__(self) -> 'Pin':
        return Pin().let(Invert(self))



class Primary:
    ins: List[Any]
    out_: Any
    def __init__(self, *args) -> None:
        self.ins = list(args)

class Or(Primary):
    def __init__(self, l, r) -> None:
        super().__init__(l, r)
class Xor(Primary):
    def __init__(self, l, r) -> None:
        super().__init__(l, r)
class And(Primary):
    def __init__(self, l, r) -> None:
        super().__init__(l, r)
class Add(Primary):
    def __init__(self, l, r) -> None:
        super().__init__(l, r)

class Invert(Primary):
    def __init__(self, l) -> None:
        super().__init__(l)


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

class IOPin:
    value: Pin

    def __init__(self, name: str = gen_id()) -> None:
        self.value = Pin(name)

    def get(self) -> Pin:
        return self.value

class Input(IOPin):
    ...

class Output(IOPin):
    ...