import pytest
import yamh

def test_bytes():
    h = yamh.murmur3_32()
    h.update(b'1234')
    assert h.digest() == 1914461635


def test_byte_array():
    h = yamh.murmur3_32()
    b = bytearray(b'1234')
    h.update(b)
    assert h.digest() == 1914461635


def test_memory_view():
    h = yamh.murmur3_32()
    b = bytearray(b'1234')
    mv = memoryview(b)
    h.update(mv)
    assert h.digest() == 1914461635


def test_memory_view_slice():
    h = yamh.murmur3_32()
    b = bytearray(b'12345')
    mv = memoryview(b)
    h.update(mv[:4])
    assert h.digest() == 1914461635
