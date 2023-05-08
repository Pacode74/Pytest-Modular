# conftest.py
import pytest
from datetime import datetime, timedelta
from typing import Callable, List, Any

# from apps.modular import Mod
from modular_arithmetics.apps.modular import Mod

from faker import Faker


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


# ------------ use it in test_simple_1--------------------------------
@pytest.fixture(params=[(5, 12)])
def demo_fixture(request):
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
