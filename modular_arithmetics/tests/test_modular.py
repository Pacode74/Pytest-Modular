# test_modular.py
import types
import pytest
import inspect
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
from pytest_check import check  # test multiple fails per test

# --------in case I want to apply the same marker for all below pytest use below. xyz is the name of the marker:-----
# It is a modular fixture. This means that every test function in this file after `pytestmark = pytest.mark.xyz` will
# have this decorator.
# pytestmark = pytest.mark.xyz or pytestmark = [pytest.mark.xyz, pytest.mark.abc]

# to test specific test write: $ pytest -k name_of_the_test
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


def test_simple_1(demo_fixture) -> None:
    """The same test as above except we use fixture from conftest.py"""
    value, modulus = demo_fixture
    m = Mod(value=value, modulus=modulus)
    assert int(m) == 5


"""Easy Level Test - test the program runs correctly
given the correct input information."""


@pytest.mark.parametrize(
    "value,modulus, expected",
    [
        (5, 12, "Mod(value=5, modulus=12)"),
        (17, 12, "Mod(value=5, modulus=12)"),
        (-7, 12, "Mod(value=5, modulus=12)"),
        (29, 12, "Mod(value=5, modulus=12)"),
        (41, 12, "Mod(value=5, modulus=12)"),
        (8, 3, "Mod(value=2, modulus=3)"),
        (1, 3, "Mod(value=1, modulus=3)"),
        (9, 5, "Mod(value=4, modulus=5)"),
    ],
)
def test_repr_method(value: int, modulus: int, expected: str) -> None:
    m = Mod(value=value, modulus=modulus)
    assert repr(m) == expected


@pytest.mark.parametrize(
    "val, modul, expected_modulus",
    [
        (5, 12, 5 % 12),
        (17, 12, 17 % 12),
        (-7, 12, -7 % 12),
        (29, 12, 29 % 12),
        (41, 12, 41 % 12),
        (8, 3, 8 % 3),
        (1, 3, 1 % 3),
        (9, 5, 9 % 5),
    ],
)
def test_value_and_modulus_property(
    val: int, modul: int, expected_modulus: int
) -> None:
    m = Mod(value=val, modulus=modul)
    with check:
        assert m.value == expected_modulus
    with check:
        assert m.modulus == modul


@pytest.mark.parametrize(
    "val, modul",
    [
        (5, 12),
        (17, 12),
        (-7, 12),
        (29, 12),
        (41, 12),
        (8, 3),
        (1, 3),
        (9, 5),
    ],
)
def test_private_value_and_modulus_attributes(val: int, modul: int) -> None:
    m = Mod(value=val, modulus=modul)
    with check:
        assert m._value == val
    with check:
        assert m._modulus == modul


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
def test_int(value: int, modulus: int, expected: int) -> None:
    m = Mod(value=value, modulus=modulus)
    assert int(m) == expected


def test_simple_with_faker(fake) -> None:
    d = [
        {"value": fake.random_int(-50, 100), "modulus": fake.random_int(50, 100)}
        for _ in range(5)
    ]
    for dictionary in d:
        assert (
            int(Mod(dictionary["value"], dictionary["modulus"]))
            == dictionary["value"] % dictionary["modulus"]
        )


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


def test_raise_type_exception_should_pass_easy() -> None:
    """test that will catch TypeError exception when it is risen
    and test that the text of the exception is correct"""
    with pytest.raises(TypeError) as e:
        Mod("a", 1)
    assert "Unsupported type for value, it must be an integer, whole number." == str(
        e.value
    )


@pytest.mark.parametrize(
    "value,modulus",
    [
        (r, 3)
        for r in [
            [1, 2, 3],
            "John",
            None,
            2j + 1,
            0.1,
            -0.5,
            "",
            int,
            str,
            float,
            complex,
            list,
            tuple,
            range,
            dict,
            set,
            frozenset,
        ]
    ],
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
    "value,modulus",
    [
        (3, r)
        for r in [
            [1, 2, 3],
            "John",
            None,
            2j + 1,
            0.1,
            "",
            int,
            str,
            float,
            complex,
            list,
            tuple,
            range,
            dict,
            set,
            frozenset,
        ]
    ],
)
def test_raise_type_exception_should_pass_parameterize_modulus(
    value: int, modulus: int
) -> None:
    with pytest.raises(TypeError) as e:
        Mod(value=value, modulus=modulus)
    assert "Unsupported type for modulus, it must be an integer, whole number." == str(
        e.value
    )


@pytest.mark.parametrize("value,modulus", [(3, -1), (3, -7), (3, -10), (5, -5)])
def test_raise_value_exception_should_pass_parameterize_modulus(
    value: int, modulus: int
) -> None:
    with pytest.raises(ValueError) as e:
        Mod(value=value, modulus=modulus)
    assert "Modulus must be greater than zero." == str(e.value)


@pytest.mark.parametrize("instance_one", [[(7, 13), (8, 14)]], indirect=True)
@pytest.mark.parametrize("instance_two", [[(19, 11), (20, 12)]], indirect=True)
def test_raise_value_exception_should_pass_parameterize_modulus_are_the_same(
    instance_one: list[Mod], instance_two: list[Mod]
) -> None:
    """The test passes if compared modulus are not the same. Normally, ValueError
    should be rasen if modulus are different when we compare instances."""
    # print(f"{instance_one=}")
    # print(f"{instance_two=}")
    for i, j in zip(instance_one, instance_two):
        with pytest.raises(ValueError) as e:
            assert i == j
            # assert i >= j
            # assert i > j
            # t = i + j
            # t = i * j
            # t = i - j
            # t = i**j

        assert "Modulus in the objects must be the same." == str(e.value)


@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2",
    [
        (7, 13, 7, 14),
        (8, 11, 21, 12),
        (15, 8, 17, 7),
        (-7, 4, 12, 2),
    ],
)
def test_raise_value_exception_should_pass_parameterize_modulus_are_the_same_v2(
    value1: int, modulus1: int, value2: int, modulus2: int
) -> None:
    instance_one = Mod(value=value1, modulus=modulus1)
    instance_two = Mod(value=value2, modulus=modulus2)
    with pytest.raises(ValueError) as e:
        with check:
            assert instance_one == instance_two
        with check:
            assert instance_one >= instance_two
    assert "Modulus in the objects must be the same." == str(e.value)


@pytest.mark.parametrize("instance_one", [[(7, 13), (8, 14)]], indirect=True)
def test_raise_type_exception_should_pass_parameterize_incompatable_type(
    instance_one: list[Mod],
) -> None:
    print(f"{instance_one=}")
    for mod in instance_one:
        with pytest.raises(TypeError) as e:
            mod + [1, 2, 3]
        assert "Incompatable types" == str(e.value)


# ----Test Comparison operators --------------------------
@pytest.mark.parametrize("instance_one", [[(7, 12), (8, 12)]], indirect=True)
@pytest.mark.parametrize("instance_two", [[(19, 12), (20, 12)]], indirect=True)
def test_equality(instance_one: list[Mod], instance_two: list[Mod]) -> None:
    """See below Notes (2)"""
    # print(f"{instance_one=}")
    # print(f"{instance_two=}")
    for i, j in zip(instance_one, instance_two):
        assert i == j


@pytest.mark.parametrize("instance_one", [[(8, 12), (9, 12)]], indirect=True)
@pytest.mark.parametrize("instance_two", [[(19, 12), (20, 12)]], indirect=True)
def test_not_equality(instance_one: list[Mod], instance_two: list[Mod]) -> None:
    """See below Notes (2)"""
    # print(f"{instance_one=}")
    # print(f"{instance_two=}")
    for i, j in zip(instance_one, instance_two):
        assert i != j


@pytest.mark.parametrize("instance_one", [[(7, 12), (8, 12)]], indirect=True)
@pytest.mark.parametrize("instance_two", [[(8, 12), (9, 12)]], indirect=True)
def test_less_than(instance_one: list[Mod], instance_two: list[Mod]) -> None:
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
    """See below Notes (2). Useful Test for the future testing."""
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


# ---------- test hash-----------------------------
@pytest.mark.parametrize("inst_one", [[(7, 12), (8, 12)]], indirect=True)
@pytest.mark.parametrize("inst_two", [[(19, 12), (20, 12)]], indirect=True)
def test_hash(inst_one: list[Mod], inst_two: list[Mod]) -> None:
    """The test passes if compared modulus are not the same. Normally, ValueError
    should be rasen if modulus are different when we compare instances.
    Explanation of the test see below Notes (2)"""
    # print(f"{instance_one=}")
    # print(f"{instance_two=}")
    for i, j in zip(inst_one, inst_two):
        assert i == j


# --------- test addition---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (9, 5, 7, 5, "Mod(value=1, modulus=5)"),
        (14, 5, 17, 5, "Mod(value=1, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=4, modulus=7)"),
        (-7, 4, 12, 4, "Mod(value=1, modulus=4)"),
    ],
)
def test_addition(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    addition = Mod(value=value1, modulus=modulus1) + Mod(value=value2, modulus=modulus2)
    with check:
        assert repr(addition) == expected
    addition2 = Mod((value1 + value2), modulus=modulus1)
    with check:
        assert repr(addition2) == expected

    addition3 = Mod(value=value1, modulus=modulus1) + value2
    with check:
        assert repr(addition3) == expected


# --------- test in-place addition---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (9, 5, 7, 5, "Mod(value=1, modulus=5)"),
        (14, 5, 17, 5, "Mod(value=1, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=4, modulus=7)"),
        (-7, 4, 12, 4, "Mod(value=1, modulus=4)"),
    ],
)
def test_in_place_addition(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    m1 = Mod(value=value1, modulus=modulus1)
    m2 = Mod(value=value2, modulus=modulus2)
    m1 += m2
    with check:
        assert repr(m1) == expected
    mm1 = Mod(value=value1, modulus=modulus1)
    mm1 += value2
    with check:
        assert repr(mm1) == expected


# --------- test subtraction---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (6, 13, 4, 13, "Mod(value=2, modulus=13)"),
        (9, 5, 7, 5, "Mod(value=2, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=5, modulus=7)"),
        (-3, 8, -6, 8, "Mod(value=3, modulus=8)"),
    ],
)
def test_subtraction(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    subtraction = Mod(value=value1, modulus=modulus1) - Mod(
        value=value2, modulus=modulus2
    )
    with check:
        assert repr(subtraction) == expected
    subtraction2 = Mod((value1 - value2), modulus=modulus1)
    with check:
        assert repr(subtraction2) == expected
    subtraction3 = Mod(value=value1, modulus=modulus1) - value2
    with check:
        assert repr(subtraction3) == expected


# --------- test in-place subtraction---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (6, 13, 4, 13, "Mod(value=2, modulus=13)"),
        (9, 5, 7, 5, "Mod(value=2, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=5, modulus=7)"),
        (-3, 8, -6, 8, "Mod(value=3, modulus=8)"),
    ],
)
def test_in_place_subtraction(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    m1 = Mod(value=value1, modulus=modulus1)
    m2 = Mod(value=value2, modulus=modulus2)
    m1 -= m2
    with check:
        assert repr(m1) == expected
    mm1 = Mod(value=value1, modulus=modulus1)
    mm1 -= value2
    with check:
        assert repr(mm1) == expected


# --------- test multiplication---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (9, 5, 7, 5, "Mod(value=3, modulus=5)"),
        (14, 5, 17, 5, "Mod(value=3, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=3, modulus=7)"),
        (-7, 4, 12, 4, "Mod(value=0, modulus=4)"),
    ],
)
def test_multiplication(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    addition = Mod(value=value1, modulus=modulus1) * Mod(value=value2, modulus=modulus2)
    with check:
        assert repr(addition) == expected
    addition2 = Mod((value1 * value2), modulus=modulus1)
    with check:
        assert repr(addition2) == expected

    addition3 = Mod(value=value1, modulus=modulus1) * value2
    with check:
        assert repr(addition3) == expected


# --------- test in-place multiplication---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (9, 5, 7, 5, "Mod(value=3, modulus=5)"),
        (14, 5, 17, 5, "Mod(value=3, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=3, modulus=7)"),
        (-7, 4, 12, 4, "Mod(value=0, modulus=4)"),
    ],
)
def test_in_place_multiplication(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    m1 = Mod(value=value1, modulus=modulus1)
    m2 = Mod(value=value2, modulus=modulus2)
    m1 *= m2
    with check:
        assert repr(m1) == expected
    mm1 = Mod(value=value1, modulus=modulus1)
    mm1 *= value2
    with check:
        assert repr(mm1) == expected


# --------- test power---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (9, 5, 7, 5, "Mod(value=4, modulus=5)"),
        (14, 5, 17, 5, "Mod(value=4, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=1, modulus=7)"),
        (-7, 4, 12, 4, "Mod(value=1, modulus=4)"),
    ],
)
def test_power(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    addition = Mod(value=value1, modulus=modulus1) ** Mod(
        value=value2, modulus=modulus2
    )
    with check:
        assert repr(addition) == expected
    addition2 = Mod((value1**value2), modulus=modulus1)
    with check:
        assert repr(addition2) == expected

    addition3 = Mod(value=value1, modulus=modulus1) ** value2
    with check:
        assert repr(addition3) == expected


# --------- test in-place power---------------------------
@pytest.mark.parametrize(
    "value1, modulus1, value2, modulus2, expected",
    [
        (9, 5, 7, 5, "Mod(value=4, modulus=5)"),
        (14, 5, 17, 5, "Mod(value=4, modulus=5)"),
        (15, 7, 17, 7, "Mod(value=1, modulus=7)"),
        (-7, 4, 12, 4, "Mod(value=1, modulus=4)"),
    ],
)
def test_in_place_power(
    value1: int, modulus1: int, value2: int, modulus2: int, expected: str
) -> None:
    m1 = Mod(value=value1, modulus=modulus1)
    m2 = Mod(value=value2, modulus=modulus2)
    m1 **= m2
    with check:
        assert repr(m1) == expected
    mm1 = Mod(value=value1, modulus=modulus1)
    mm1 **= value2
    with check:
        assert repr(mm1) == expected


# --------- test addition, subtraction, multiplication---------------------------
@pytest.mark.parametrize(
    "v1, v2, v3, v4, modulus, expected",
    [
        (9, 7, 1, 20, 5, "Mod(value=1, modulus=5)"),
        (14, 17, 41, 3, 5, "Mod(value=3, modulus=5)"),
        (14, -17, 41, 3, 7, "Mod(value=5, modulus=7)"),
        (-14, -17, -41, -3, 12, "Mod(value=2, modulus=12)"),
    ],
)
def test_various_operations(
    v1: int, v2: int, v3: int, v4: int, modulus: int, expected: str
) -> None:
    total = (Mod(value=v1, modulus=modulus) + Mod(value=v2, modulus=modulus)) * (
        Mod(value=v3, modulus=modulus) - Mod(value=v4, modulus=modulus)
    )
    with check:
        assert repr(total) == expected
    total = Mod(((v1 + v2) * (v3 - v4)), modulus=modulus)
    with check:
        assert repr(total) == expected

    total = (Mod(value=v1, modulus=modulus) + v2) * (v3 - v4)
    with check:
        assert repr(total) == expected


# --------- test negative value---------------------------
@pytest.mark.parametrize(
    "value, modulus, expected",
    [
        (-9, 5, Mod(-9, 5)),
        (-14, 5, Mod(-14, 5)),
        (-15, 7, Mod(-15, 7)),
        (-7, 4, Mod(-7, 4)),
    ],
)
def test_negative_value_argument(value: int, modulus: int, expected: Mod) -> None:
    m = Mod(value=value, modulus=modulus)
    assert m.__neg__() == expected.__neg__()


# ------------- Extra tests -----------------------------
# ----------- test that class is a type instance --------
def test_mod_is_instance_of_type() -> None:
    assert isinstance(Mod, type)


# --test that Mod class has 3 attributes --
def test_instance_has_three_attrs() -> None:
    """Test that class has 3 attrs ['convert_integer_to_modular_and_check_modulus_the_same', 'modulus', 'value']"""
    m = Mod(value=9, modulus=5)
    actual = len([attr for attr in dir(m) if not attr.startswith("_")])
    expected = 3
    assert actual == expected, f"Mod class does not have {expected} attributes."


def test_instance_has_three_attributes() -> None:
    """Test that class has 3 attrs ['convert_integer_to_modular_and_check_modulus_the_same', 'modulus', 'value']"""
    m = Mod(value=9, modulus=5)
    attributes = [attr for attr in dir(m) if not attr.startswith("_")]
    for attr in attributes:
        msg = f"The Mod instance does not have a {attr} attribute."
        assert hasattr(m, attr), msg


def test_if_three_attributes_belong_to_class() -> None:
    """Test that class has 3 attrs ['convert_integer_to_modular_and_check_modulus_the_same', 'modulus', 'value']"""
    m = Mod(value=9, modulus=5)
    attributes = [attr for attr in dir(m) if not attr.startswith("_")]
    for attr in attributes:
        msg = f"{attr} attribute is not in instance scope."
        with check:
            assert attr in Mod.__dict__, msg
        with check:
            assert attr in type(m).__dict__, msg
        with check:
            assert attr in m.__class__.__dict__, msg
        # assert attr in m.__dict__, msg


def test_if_two_attributes_belong_to_instance() -> None:
    """Test that class has 3 attrs ['_modulus', '_value']"""
    m = Mod(value=9, modulus=5)
    with check:
        assert "_modulus" in m.__dict__
    with check:
        assert "_value" in m.__dict__


def test_instance_has__value__modulus_attributes() -> None:
    m = Mod(value=9, modulus=5)
    attributes = ["_value", "_modulus"]
    for attr in attributes:
        msg = f"The Mod instance does not have {attr} attribute."
        assert hasattr(m, attr), msg


def test_value_is_property() -> None:
    with check:
        assert isinstance(Mod.value, property)
    # alternatively:
    with check:
        assert isinstance(inspect.getattr_static(Mod, "value"), property)


def test_modulus_is_property() -> None:
    with check:
        assert isinstance(Mod.value, property)
    # alternatively:
    with check:
        assert isinstance(inspect.getattr_static(Mod, "modulus"), property)


def test_convert_integer_to_modular_and_check_mudulus_the_same_is_function() -> None:
    with check:
        assert isinstance(
            Mod.__dict__["convert_integer_to_modular_and_check_mudulus_the_same"],
            types.FunctionType,
        )
    with check:
        assert isinstance(
            inspect.getattr_static(
                Mod, "convert_integer_to_modular_and_check_mudulus_the_same"
            ),
            types.FunctionType,
        )


def test_convert_integer_to_modular_and_check_mudulus_the_same_function_is_callable() -> (
    None
):
    assert callable(
        Mod.convert_integer_to_modular_and_check_mudulus_the_same
    ), f"'convert_integer_to_modular_and_check_mudulus_the_same' is not callable."


def test_attributes_value_and_modulus_are_not_callable() -> None:
    with check:
        assert not callable(Mod.value), f"'value' is callable."
    with check:
        assert not callable(Mod.modulus), f"'modulus' is callable."
