from nis import match
from typing import Type
from datatype import YLObject



class RawModule(YLObject):
    pass


class Module(RawModule):
    pass


def yl(cls: Type[YLObject]):
    
    # name binding
    for k, v in filter(lambda pair: isinstance(pair[1], YLObject), cls.__dict__.items()):
        v.bindname = "{}_{}".format(cls.__name__, k)

    try:
        cls.__dict__['io'] = yl(cls.__dict__['io'])
    except:
        pass
    return cls
