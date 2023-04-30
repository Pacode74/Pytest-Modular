# test_modular.py
import pytest
from typing import Callable, List, Any
from modular_arithmetics.apps.modular import Mod


## in case I want to apply the same marker for all below pytest use below.
## xyz is the name of the marker:
# pytestmark = pytest.mark.xyz


# ----------Basic Level Tests: test Mod with different numbers--------------------
def test_simple() -> None:
    m = Mod(value=8, modulus=3)
    assert int(m) == 2

    m = Mod(value=1, modulus=3)
    assert int(m) == 1

    m = Mod(value=5, modulus=7)
    assert int(m) == 5

    m = Mod(value=9, modulus=5)
    assert int(m) == 4


"""Easy Level Test - test the program runs correctly
given the correct input information."""


@pytest.mark.parametrize(
    "value,modulus, expected",
    [
        (5, 12, 5),
        (17, 12, 5),
        (-7, 12, 5),
        (29, 12, 5),
        (41, 12, 5),
        (8, 3, 2),
        (1, 3, 1),
        (9, 5, 4),
    ],
)
def test_simple_numbers(value: int, modulus: int, expected: int) -> None:
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


# ------------------Test exceptions raised and text of exception correct-----------------------
"""Medium Level Test - test the program runs correctly
given the wrong input information."""


def test_raise_type_exception_should_pass() -> None:
    """test that will catch TypeError exception when it is risen
    and test that the text of the exception is correct"""
    with pytest.raises(TypeError) as e:
        Mod("a", 1)
    assert "Unsupported type for value, it must be an integer, whole number." == str(
        e.value
    )


@pytest.mark.parametrize(
    "value,modulus", [("a", 3), ([1, 2, 3], 3), (0.1, 3), (2j + 1, 5)]
)
def test_raise_type_exception_should_pass_parameterize(
    value: int, modulus: int
) -> None:
    """The same test as above except now we use different parameters."""
    with pytest.raises(TypeError) as e:
        Mod(value=value, modulus=modulus)
    assert "Unsupported type for value, it must be an integer, whole number." == str(
        e.value
    )


# ----Test two functions allowed to take same arguments or test two functions allowed to take different arguments ------


def mod_expected(a) -> List:
    """This function is used for below test_two_functions_outside_conftest_take_the_same_arguments_v1"""
    return [value % a for value in range(1, a + 1)]


def mod_actual(a) -> List:
    """This function is used for below test_two_functions_outside_conftest_take_the_same_arguments_v1"""
    return [int(Mod(value, a)) for value in range(1, a + 1)]


@pytest.mark.parametrize(
    "mod_func_class",
    [mod_expected, mod_actual],
)
@pytest.mark.parametrize(
    "n, expected",
    [
        (11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]),
        (12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]),
    ],
)
def test_two_functions_outside_conftest_take_the_same_arguments_v1(
    time_tracker, mod_func_class: Callable[[int], int], n: int, expected: List
) -> None:
    """Two functions mod_expected and mod_actual are outside conftest.py.
    Testing that if they take the same n argument the expected lists are the same.
    mod_func_class is not a fixture."""
    res = mod_func_class(n)
    # print(f'{res=}')
    # print(f'{expected=}')
    assert res == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]),
        (12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]),
    ],
)
def test_two_functions_inside_conftest_take_the_same_arguments_v2(
    time_tracker,
    mod_exp: Callable[[], list[int | Any]],
    mod_act: Callable[[], list[int | Any]],
    n: int,
    expected: List,
) -> None:
    """Two functions mod_expected and mod_actual are inside conftest.py.
    Testing that if they take the same n argument the expected lists are the same."""
    # print(f'{mod_act(n)=}')
    # print(f'{mod_exp(n)=}')
    assert mod_exp(n) == mod_act(n)


@pytest.mark.parametrize(
    "modulars_expected_actual",  # this is a fixture located in conftest
    [[5, 6], [11, 12]],  # these two list can be combined
    indirect=True,
    ids=["five and six", "eleven and twelve"],
)
def test_two_functions_inside_conftest_take_the_same_arguments_v3(
    modulars_expected_actual,
) -> None:
    """See below Notes (1)"""
    # print(f"{modulars_expected_actual=}")
    expected, actual = modulars_expected_actual
    # print(f"{expected=}")
    # print(f"{actual=}")
    # comparing two nested lists:
    assert sorted(expected) == sorted(actual)


@pytest.mark.parametrize(
    "modulars_expected",
    [[11, 12]],
    indirect=True,
    ids=["Expected eleven and twelve"],
)
@pytest.mark.parametrize(
    "modulars_actual",
    [[11, 12]],
    indirect=True,
    ids=["Actual eleven and twelve"],
)
def test_two_functions_take_different_arguments(
    modulars_expected, modulars_actual
) -> None:
    """See below Notes (2)"""
    # print(f"{modulars_expected=}")
    # print(f"{modulars_actual=}")
    # Comparing two nested lists:
    assert sorted(modulars_expected) == sorted(modulars_actual)


"""
Note:
(1) The intention of this test is to learn how to use
    two functions and test them with the same parameters. This in turn,
     should produce the same results. Because here we cannot have different paramenters in
    each function, we cannot fail the test. Using conftest.py

    Test modulars_expected_actual has two functions:
    first, is generating expected list using % and
    second, is generating actual list using Mod(). Then,
    we use the same above parameters in both functions to generate
    the test results.

(2) The intention of this test is to learn how to use
    two functions and test them with different parameters. If the parameters are
    different the test will fail. If the parameters are the same the test will pass.

    We have two functions that each generate a list:
    For example:
    [[7, another_number]]
    n = 7
    modulars_expected = [ t % n for t in range(1,n+1)]
    modulars_actual = [ int(Mod(t, n)) for t in range(1,n+1)]
    [1, 2, 3, 4, 5, 6, 0]  == [1, 2, 3, 4, 5, 6, 0]

    Then, each function takes above parameters that are for that
    particular function. Then we compare if the nested lists generated
    by each function are equal.
"""
