import pytest
import yamh


def test_hash_values():
    h = yamh.murmur3_32()
    h.update(b'')
    assert h.digest() == 0
    h = yamh.murmur3_32()
    h.update(b'1')
    assert h.digest() == 2484513939
    h = yamh.murmur3_32()
    h.update(b'12')
    assert h.digest() == 4191350549
    h = yamh.murmur3_32()
    h.update(b'123')
    assert h.digest() == 2662625771
    h = yamh.murmur3_32()
    h.update(b'1234')
    assert h.digest() == 1914461635
    h = yamh.murmur3_32()
    h.update(b'12345')
    assert h.digest() == 329585043
    h = yamh.murmur3_32()
    h.update(b'123456')
    assert h.digest() == 3210799800
    h = yamh.murmur3_32()
    h.update(b'1234567')
    assert h.digest() == 3085927159
    h = yamh.murmur3_32()
    h.update(b'12345678')
    assert h.digest() == 2444432334
