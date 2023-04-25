import pytest
from modular_arithmetics.apps.modular import Mod
from time import sleep

## Option 1: Result is the same as option 2. I separated decorator and fixture:
# from modular_arithmetics.apps.track_performance_decorator import track_performance_decorator

# Option 2: Result is the same as option 1. Teacher didn't separate decorator and fixture:
from modular_arithmetics.tests.conftest import track_performance_decorator


@pytest.mark.performance
@track_performance_decorator
def test_performance():
    """1) mark it with performance marker that is registered in pytest.ini.
    2) decorate it track_performance_decorator"""
    # sleep(3)
    Mod(6, 19) ** Mod(7, 19)
