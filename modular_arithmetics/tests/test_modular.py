import pytest
from typing import Callable
from modular_arithmetics.apps.modular import Mod


def test_mod() -> None:
    m = Mod(value=8, modulus=3)
    assert int(m) == 2

    m = Mod(value=1, modulus=3)
    assert int(m) == 1

    m = Mod(value=5, modulus=7)
    assert int(m) == 5

    m = Mod(value=9, modulus=5)
    assert int(m) == 4


@pytest.mark.parametrize(
    "value,modulus, expected", [(8, 3, 2), (1, 3, 1), (5, 7, 5), (9, 5, 4)]
)
def test_mod(value: int, modulus: int, expected: int) -> None:
    m = Mod(value=value, modulus=modulus)
    assert int(m) == expected


@pytest.mark.parametrize("mod_instance", [Mod])
@pytest.mark.parametrize(
    "value,modulus, expected", [(8, 3, 2), (1, 3, 1), (5, 7, 5), (9, 5, 4)]
)
def test_mod_time_tracker(
    time_tracker,
    mod_instance: Callable[[int], int],
    value: int,
    modulus: int,
    expected: int,
) -> None:
    """The same tests as above except that we add a time_tracker for each test now."""
    m = Mod(value=value, modulus=modulus)
    assert int(m) == expected


def test_raise_type_exception_should_pass() -> None:
    """test that will catch TypeError exception when it is risen
    and test that the text of the exception is correct"""
    with pytest.raises(TypeError) as e:
        Mod('a', 1)
    assert "Unsupported type for value, it must be an integer, whole number." == str(e.value)


@pytest.mark.parametrize(
    "value,modulus", [('a', 3), ([1, 2, 3], 3), (0.1, 3), (2j+1, 5)]
)
def test_mod(value: int, modulus: int) -> None:
    with pytest.raises(TypeError) as e:
        Mod(value=value, modulus=modulus)
    assert "Unsupported type for value, it must be an integer, whole number." == str(e.value)

