import pytest

@pytest.fixture
def prepared_data():
    data = [1, 2, 3, 4, 5]
    processed_data = [x * 2 for x in data]
    return processed_data

def test_processed_data(prepared_data):
    assert prepared_data == [2, 4, 6, 8, 10]

def test_addition():
    assert 2 + 2 == 4


@pytest.mark.parametrize("test_input, expected_output", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected_output):
    assert eval(test_input) == expected_output



class Calculator:
    def add(self, a, b):
        return a + b

@pytest.fixture
def calculator():
    return Calculator()

def test_addition1(calculator):
    result = calculator.add(2, 2)
    assert result == 4