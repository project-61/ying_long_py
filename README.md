# YingLong Frontend implmented by Python

The YingLong HDL Python frontend implementation.

## example

```python
class alu(RawModule):
    a = Input(Int(32))
    b = Input(Int(32))
    c = Output(Int(32))

    c = a + b

class top(Module):
    i = Input(Int(32))
    o = Output(Int(32))

    r = Reg(Int(32)) # Equivalent to Reg(Int(32), clk=self.clk)

    o = r

    r = r + i
```

```python
# Test

def drive_once(top_level: top, i: value) -> int:
    top_level.i = i
    top_level.clk_once()
    return top_level.o

def test():
    top = top.crate_toplevel_env()
    result = [drive_once(top, i) for i in range(0, 2)]
    assert result == [0, 0, 1, 3]
```
