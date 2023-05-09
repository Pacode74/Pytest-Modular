# conftest.py
import pytest
from datetime import datetime, timedelta
from typing import Callable, List, Any

# from apps.modular import Mod
from modular_arithmetics.apps.modular import Mod

from faker import Faker
from modular_arithmetics.apps.creating_data import data

# ----------use it in test_mod_time_tracker-------------
@pytest.fixture
def time_tracker():
    """In order to use the time tracker in our test we need to mark it as a fixture."""
    start = datetime.now()
    yield  # yield and pass the cpu to run the test
    end = datetime.now()
    diff = end - start
    print(f"\n runtime: {diff.total_seconds()}")


# ------------use it in test_performance----------------


class PerformanceException(Exception):
    """Implementation of exception with details of runtime"""

    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f"Performance test failed, runtime: {self.runtime.total_seconds()}, limit: {self.limit.total_seconds()}"


def track_performance_decorator(
    method: Callable, runtime_limit=timedelta(seconds=2)
):  # (1)
    """Decorator that check the time performance of a function and
    when runtime limit is exceeded it raises Performance Exception."""

    def run_function_and_validate_runtime(*args, **kwargs):
        start = datetime.now()
        result = method(*args, **kwargs)
        end = datetime.now()
        runtime = end - start
        print(f"\n runtime: {runtime.total_seconds()}")
        # db.add(runtime)  # (2)
        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)
        return result

    return run_function_and_validate_runtime


"""
Notes:
(1) We can configure the runtime limit to be something dynamic so we can define 
dynamically a baseline that's going to be the average of all the runs of all the developers.
And that's going to be our baseline and that's going to be the runtime limit for our test.
That's a very simple example, but that's a very common use case that we can do with 
performance testing.

(2) option to monitor and save into a database the performance results of the tests.
So lets say we have a few developers in our team and we want that for each developer 
that is running our test. We want to save the result of the test in the database.
I mean, the runtime result. So we can just add this functionality in our decorator 
because we implemented it ourselves.

Important: Instead of custom decorator `track_performance_decorator` 
that we wrote above we can use `pytest-timeout` build-in decorator.  
"""


# ------------ use it in test_simple_v1 and v2--------------------------------
@pytest.fixture(params=[(5, 12)])
def demo_fixture(request):
    # print(f'{request.param=}')
    return request.param


@pytest.fixture(
    params=[
        (5, 12, "Mod(value=5, modulus=12)"),
        (17, 12, "Mod(value=5, modulus=12)"),
        (-7, 12, "Mod(value=5, modulus=12)"),
        (29, 12, "Mod(value=5, modulus=12)"),
        (41, 12, "Mod(value=5, modulus=12)"),
        (8, 3, "Mod(value=2, modulus=3)"),
        (1, 3, "Mod(value=1, modulus=3)"),
        (9, 5, "Mod(value=4, modulus=5)"),
    ]
)
def demo_fixt(request):
    # print(f'{request.param=}')
    return request.param


# -------use it in test_two_functions_take_the_same_arguments_v3 and in test_two_functions_take_different_arguments-----


@pytest.fixture
def modular_expected() -> Callable[[], list[int | Any]]:
    def _modular(*args):
        for a in args:
            return [value % a for value in range(1, a + 1)]

    return _modular


@pytest.fixture
def modulars_expected(request, modular_expected) -> list[list[int | Any]]:
    lst = []
    modulus = request.param  # this is pytest request
    for i in modulus:
        lst.append(modular_expected(i))
    return lst


@pytest.fixture
def modular_actual() -> Callable[[], list[int | Any]]:
    def _modular(*args):
        for a in args:
            return [int(Mod(value, a)) for value in range(1, a + 1)]

    return _modular


@pytest.fixture
def modulars_actual(request, modular_actual) -> list[list[int]]:
    lst = []
    modulus = request.param  # this is pytest request
    for i in modulus:
        lst.append(modular_actual(i))
    return lst


@pytest.fixture
def modulars_expected_actual(request, modular_actual, modular_expected) -> List[int]:
    modulus = request.param
    lst_actual = [modular_actual(i) for i in modulus]
    lst_expected = [modular_expected(i) for i in modulus]
    return lst_expected, lst_actual


# ---------------it is used in test_two_functions_inside_conftest_take_the_same_arguments_v2--------------
@pytest.fixture
def mod_exp() -> Callable[[], list[int | Any]]:
    def _modular(a):
        return [value % a for value in range(1, a + 1)]

    return _modular


@pytest.fixture
def mod_act() -> Callable[[], list[int | Any]]:
    def _modular(a):
        return [int(Mod(value, a)) for value in range(1, a + 1)]

    return _modular


# ------------it is used in test_raise_value_exception_should_pass_parameterize_modulus_are_the_same---------


@pytest.fixture
def instance_one(request) -> list[Mod]:
    value_modulus = request.param
    # print(f'value_modulus1={value_modulus}')
    lst = [Mod(value, modulus) for value, modulus in value_modulus]
    return lst


@pytest.fixture
def instance_two(request) -> list[Mod]:
    value_modulus = request.param
    # print(f'value_modulus2={value_modulus}')
    lst = [Mod(value, modulus) for value, modulus in value_modulus]
    return lst


# ---------------- using in test_hash -----------------------
@pytest.fixture
def inst_one(request) -> list[int]:
    value_modulus = request.param
    # print(f'value_modulus1={value_modulus}')
    lst = [hash(Mod(value, modulus)) for value, modulus in value_modulus]
    return lst


@pytest.fixture
def inst_two(request) -> list[int]:
    value_modulus = request.param
    # print(f'value_modulus2={value_modulus}')
    lst = [hash(Mod(value, modulus)) for value, modulus in value_modulus]
    return lst


# ----- for faker, used in test_simple_with_faker ------


@pytest.fixture
def fake():
    fake = Faker()
    fake.seed_instance(1234)
    return fake


# ----------------------------test congruence list------------


@pytest.fixture
def congruent_list() -> Callable[[Any, Any, int, int], list[int]]:
    def _congruent_list(
        modulus: int, remainder: int, start_num: int = 1, end_num: int = 100
    ):
        return [
            num for num in range(start_num, end_num + 1) if num % modulus == remainder
        ]

    return _congruent_list


@pytest.fixture
def remainder_list(congruent_list) -> Callable[[Any, Any, int, int], list[int]]:
    def _remainder_list(
        modulus: int,
        remainder: int,
        start_num: int = 1,
        end_num: int = 100,
        congruent_list=congruent_list,
    ):
        congruent_list = congruent_list(
            modulus=modulus, remainder=remainder, start_num=start_num, end_num=end_num
        )
        return [(value % modulus) for value in congruent_list]

    return _remainder_list

@pytest.fixture
def params_values_are_property() -> None:
    def _params_values_are_property(modulus: int, remainder: int, start_num: int = 1, end_num: int = 100):
        congruent_list = [num for num in range(start_num, end_num + 1) if num % modulus == remainder]
        remainder_list = [(value % modulus) for value in congruent_list]
        mod_list_value_property = [f'{Mod(value, modulus)}' for value in congruent_list]
        params = [(value, modulus, mod) for value, mod in zip(congruent_list, mod_list_value_property)]
        return params, remainder_list, congruent_list
    yield _params_values_are_property

@pytest.fixture
def parameters() -> None:
    def _parameters(modulus: int, remainder: int, value_property=True, start_num: int = 1, end_num: int = 100):
        congruent_list = [num for num in range(start_num, end_num + 1) if num % modulus == remainder]
        remainder_list = [(value % modulus) for value in congruent_list]
        if value_property:
            mod_list_value_property = [f'{Mod(value, modulus)}' for value in congruent_list]
            params = [(value, modulus, mod) for value, mod in zip(congruent_list, mod_list_value_property)]
            return params, #remainder_list, congruent_list
        else:
            mod_list_value_property = [f'Mod(value={value}, modulus={modulus})' for value in congruent_list]
            params = [(value, modulus, mod) for value, mod in zip(congruent_list, mod_list_value_property)]
            return params, #remainder_list, congruent_list
    yield _parameters


@pytest.fixture
def param() -> None:
    congruent_list = []
    remainder_list = []
    mod_list_value_property = []
    mod_list_value_private = []
    params_list = []
    def _parameters(modulus: int, remainder: int, value_property=True, start_num: int = 1, end_num: int = 100):
        # Loop through the range of numbers and check for congruence
        for num in range(start_num, end_num + 1):
            if num % modulus == remainder:
                congruent_list.append(num)

        # create remainder list
        for value in congruent_list:
            remainder_list.append(value % modulus)

        if value_property:
            for value in congruent_list:
                mod_list_value_property.append(f'Mod(value={value%modulus}, modulus={modulus})')

            for value, mod in zip(congruent_list, mod_list_value_property):
                params_list.append((value, modulus, mod))

            return params_list, remainder_list, congruent_list
        else:
            for value in congruent_list:
                mod_list_value_private.append(f'Mod(value={value}, modulus={modulus})')

            for value, mod in zip(congruent_list, mod_list_value_private):
                params_list.append((value, modulus, mod))

            return params_list, remainder_list, congruent_list
    yield _parameters
    del congruent_list[:]
    del remainder_list[:]
    del mod_list_value_property[:]
    del mod_list_value_private[:]
    del params_list[:]

@pytest.fixture(params=data(modulus=5, remainder=2, value_property=True))
def data_conftest(request):
    # print(f'{request.param=}')
    return request.param

