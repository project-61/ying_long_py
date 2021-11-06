

from typing import ClassVar, Optional
from ying_long_py.pin import Clock, Input, Output, Pin


# Trigger
class Tr:
    posedge: int = 1
    negedge: int = 2
    any_case: int = posedge | negedge

    trigger_type: int
    signal: Clock
    def __init__(self, signal: Clock, trigger_type: int = any_case) -> None:
        self.signal = signal
        self.trigger_type = trigger_type


class Initial:
    pass


class Always:
    pass


class Mod:
    input: ClassVar[Input] = Input()
    Output: ClassVar[Output] = Output()

    def initial(self) -> Optional[Initial]:
        return None

    def always(self, *args: Tr) -> Optional[Always]:
        return None
