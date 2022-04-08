from multiprocessing.spawn import old_main_modules
from main import isEven
import pytest

# sudo apt install python3-pip
# pip3 install pytest --user
# pip3 install pytest-fixture --user

# Autouse fixtures are meant for startup and teardown
# If you want the return value from a fixture, you must
# specify it in a parameter
@pytest.fixture(autouse=True)
def printWelcome():
    print("Starting tests!")

@pytest.fixture()
def evenNumbers():
    return [2,4]

@pytest.fixture
def oddNumbers():
    return [1,3]

def test_isEven_even(evenNumbers):
    for num in evenNumbers:
        assert isEven(num);

def test_isEven_odd(oddNumbers):
    for num in oddNumbers:
        assert not isEven(num);
