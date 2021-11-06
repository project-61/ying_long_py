

from typing import ClassVar, Optional, Type, Union
from ying_long_py.pin import Clock, Input, Output, Pin


class TriggerType:...

class Posedge(TriggerType):...
class Negedge(TriggerType):...
class AnyCase(Posedge, Negedge):...

# Trigger
class Trigger:
    trigger_type: int
    # signal: Clock
    #def __init__(self, signal: Clock, trigger_type: int = any_case) -> None:
    #    self.signal = signal
    #    self.trigger_type = trigger_type
    # @staticmethod
    # def posedge()


class Initial:
    pass


class Always:
    pass


class Mod:
    name: ClassVar[str]
    # input: ClassVar[Input] = Input()
    # Output: ClassVar[Output] = Output()

    # def initial(self) -> Optional[Initial]:
        # return None

    # def always(self, *args: Tr) -> Optional[Always]:
        # return None
