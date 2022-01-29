from typing import Optional, Type, Union, List


class YLObject:
    bindname: str
    wiresize: int
    def get_wiresize(self) -> int:
        return self.wiresize


class Op(YLObject):
    def __add__(self, other: 'Op') -> 'Op':
        return Add(self, other)

    def __sub__(self, other: 'Op') -> 'Op':
        return Sub(self, other)

    def __mul__(self, other: 'Op') -> 'Op':
        return Mul(self, other)

    def __truediv__(self, other: 'Op') -> 'Op':
        return Div(self, other)

    def __mod__(self, other: 'Op') -> 'Op':
        return Mod(self, other)

    def __and__(self, other: 'Op') -> 'Op':
        return And(self, other)

    def __or__(self, other: 'Op') -> 'Op':
        return Or(self, other)

    def __xor__(self, other: 'Op') -> 'Op':
        return Xor(self, other)

    def __not__(self) -> 'Op':
        return Not(self)

    def __lshift__(self, size: int) -> 'Op':
        return Shl(self, size)

    def __rshift__(self, size: int) -> 'Op':
        return Shr(self, size)

    def __eq__(self, other):
        return Eq(self, other)

    def __ne__(self, other):
        return Neq(self, other)

    def __getitem__(self, i) -> 'Op':
        if isinstance(i, int):
            return WireSlice(self, i, i)
        elif isinstance(i, slice):
            return WireSlice(self, i.start, i.stop)
        else:
            raise TypeError("Invalid type of index")

class Wire(Op):
    source: Optional[Op]
    def __init__(self, size: int = 1):
        self.wiresize = size

    def __le__(self, other: 'Wire') -> None:
        assert self.wiresize == other.wiresize
        self.source = other


class Bundle(Wire):
    pass


class Bool(Wire):
    def __init__(self):
        super().__init__(1)


class Uint(Wire):
    def __init__(self, size: int):
        super().__init__(size)

class Int(Uint):
    def __init__(self, size: int):
        super().__init__(size)



class Operator(Op):
    pass


class UnaryOp(Operator):
    a: Op

    def __init__(self, a: Op) -> None:
        self.a = a

    def get_wiresize(self) -> int:
        return self.a.get_wiresize()


class BinaryOp(Operator):
    b: Op

    def __init__(self, a: Op, b: Op) -> None:
        assert a.wiresize == b.wiresize
        self.a = a
        self.b = b


class Add(BinaryOp):
    pass


class Sub(BinaryOp):
    pass


class Mul(BinaryOp):
    pass


class Div(BinaryOp):
    pass


class Mod(BinaryOp):
    pass


class And(BinaryOp):
    pass


class Or(BinaryOp):
    pass


class Xor(BinaryOp):
    pass


class Not(UnaryOp):
    pass


class Shl(UnaryOp):
    def __init__(self, a: Op, b: int) -> None:
        assert a.wiresize == 1
        self.a = a
        self.b = b


class Shr(UnaryOp):
    def __init__(self, a: Op, b: int) -> None:
        self.a = a
        self.b = b


# compare

class Eq(BinaryOp):
    def get_wiresize(self) -> int:
        return 1


class Neq(BinaryOp):
    def get_wiresize(self) -> int:
        return 1


class Extend(UnaryOp):
    def __init__(self, a: Op, b: int) -> None:
        assert b >= a.get_wiresize()
        self.a = a
        self.b = b

class WireSlice(UnaryOp):
    left: int
    right: int

    def __init__(self, a: Op, left: int, right: int) -> None:
        assert left >= 0 and right >= 0
        assert right < a.get_wiresize()
        self.a = a
        self.left = left
        self.right = right

    def get_wiresize(self) -> int:
        return self.right - self.left + 1


class Concat(Operator):
    wiresize: int
    wires: List[Op]

    def __init__(self, wires: List[Op]) -> None:
        self.wires = wires

    def get_wiresize(self) -> int:
        try:
            return self.wiresize
        except AttributeError:
            rsize: int = sum(w.get_wiresize() for w in self.wires)
            self.wiresize = rsize
            return self.wiresize

