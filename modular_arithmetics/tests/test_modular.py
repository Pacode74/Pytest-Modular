# test_modular.py
import pytest
from typing import Callable, List, Any
from modular_arithmetics.apps.modular import Mod
import logging
from modular_arithmetics.apps.exception_logging.exception_logging_warning_level import (
    function_that_logs_something_warning_level,
)
from modular_arithmetics.apps.exception_logging.exception_logging_info_level import (
    function_that_logs_something_info_level,
)
from modular_arithmetics.apps.exception_logging.logging_func import logger

# --------in case I want to apply the same marker for all below pytest use below. xyz is the name of the marker:-----
# It is a modular fixture. This means that every test function in this file after `pytestmark = pytest.mark.xyz` will
# have this decorator.
# pytestmark = pytest.mark.xyz or pytestmark = [pytest.mark.xyz, pytest.mark.abc]


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
def test_raise_type_exception_should_pass_parameterize_value(
    value: int, modulus: int
) -> None:
    with pytest.raises(TypeError) as e:
        Mod(value=value, modulus=modulus)
    assert "Unsupported type for value, it must be an integer, whole number." == str(
        e.value
    )


@pytest.mark.parametrize(
    "value,modulus", [(3, "a"), (3, [1, 2, 3]), (3, 0.1), (5, 2j + 1)]
)
def test_raise_type_exception_should_pass_parameterize_modulus(
    value: int, modulus: int
) -> None:
    with pytest.raises(TypeError) as e:
        Mod(value=value, modulus=modulus)
    assert "Unsupported type for modulus, it must be an integer, whole number." == str(
        e.value
    )


@pytest.mark.parametrize(
    "value,modulus", [(3, -1), (3, -7), (3, -10), (5, -5)]
)
def test_raise_value_exception_should_pass_parameterize_modulus(
    value: int, modulus: int
) -> None:
    with pytest.raises(ValueError) as e:
        Mod(value=value, modulus=modulus)
    assert "Modulus must be greater than zero." == str(
        e.value
    )



@pytest.mark.parametrize("instance_one", [[(7, 13), (8, 14)]], indirect=True)
@pytest.mark.parametrize("instance_two", [[(19, 12), (20, 12)]], indirect=True)
def test_raise_value_exception_should_pass_parameterize_modulus_are_the_same(
    instance_one: list[Mod], instance_two: list[Mod]
) -> None:
    """ The test passes if compared modulus are not the same. Normally, ValueError
    should be rasen if modulus are different when we compare instances.
    Explanation of the test see below Notes (2)"""
    # print(f"{instance_one=}")
    # print(f"{instance_two=}")
    for i, j in zip(instance_one, instance_two):
        with pytest.raises(ValueError) as e:
            assert i == j
            assert i >= j
            assert i > j
            t = i + j
            t = i * j
            t = i - j
            t = i**j

        assert "Modulus in the objects must be the same." == str(e.value)


@pytest.mark.parametrize("instance_one", [[(7, 13), (8, 14)]], indirect=True)
def test_raise_type_exception_should_pass_parameterize_incompatable_type(
    instance_one: list[Mod]) -> None:
    print(f"{instance_one=}")
    for mod in instance_one:
        with pytest.raises(TypeError) as e:
            mod + [1, 2, 3]
        assert "Incompatable types" == str(e.value)


# ----Test Comparison operators --------------------------
@pytest.mark.parametrize("instance_one", [[(7, 12), (8, 12)]], indirect=True)
@pytest.mark.parametrize("instance_two",[[(19, 12), (20, 12)]],indirect=True)
def test_equality(
    instance_one: list[Mod], instance_two: list[Mod]
) -> None:
    """See below Notes (2)"""
    # print(f"{instance_one=}")
    # print(f"{instance_two=}")
    for i, j in zip(instance_one, instance_two):
        assert i == j

@pytest.mark.parametrize("instance_one", [[(7, 12), (8, 12)]], indirect=True)
@pytest.mark.parametrize("instance_two",[[(8, 12), (9, 12)]],indirect=True)
def test_less_than(
    instance_one: list[Mod], instance_two: list[Mod]
) -> None:
    """See below Notes (2)"""
    # print(f"{instance_one=}")
    # print(f"{instance_two=}")
    for i, j in zip(instance_one, instance_two):
        assert i < j

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

# ---------------------------TestInGeneralExceptionLogging--------------------


def test_exception_logged_warning_level(caplog) -> None:
    """Testing exception was raised and logged at WARNING level"""
    function_that_logs_something_warning_level()
    assert "I am logging Modular Exception" in caplog.text


def test_exception_logged_info_level(caplog) -> None:
    """Testing exception was raised and logged at INFO level"""
    with caplog.at_level(logging.INFO):
        function_that_logs_something_info_level()
        print(f".caplog.text:{caplog.text}")
        assert "I am logging Modular Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    """Testing logging function at INFO level"""
    with caplog.at_level(logging.INFO):
        logger()  # imported from exception_logging
        print(f".caplog.text:{caplog.text}")
        assert "I am logging info level" in caplog.text
