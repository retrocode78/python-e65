from pe65.memory import Memory
import pytest


def test_mem_create():
    m = Memory(2048, 0)
    assert m.base == 0
    assert m.size == 2048


def test_mem_write_read():
    m = Memory(2048, 0)
    addr = 343
    data = 123
    m.write(addr, data)
    v = m.read(addr)
    assert data == v


def test_mem_bounds():
    m = Memory(256, 0)
    addr = 343
    data = 123

    with pytest.raises(IndexError):
        m.write(addr, data)

    with pytest.raises(IndexError):
        _ = m.read(addr)

    with pytest.raises(IndexError):
        m.write(-1, data)
