import pytest

from src.decorators import log


def test_decorator(capsys):
    """Тестируем на успешное выполнение функции"""

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert "my_function started" in captured.out
    assert "my_function is ok" in captured.out
    assert "my_function finished" in captured.out

    with open("mylog.txt", "r") as file:
        log_content = file.read()
        assert "faulty_function started" in log_content


def test_decorator_error(capsys):
    """Тестируем обработку исключений"""

    @log(filename="mylog.txt")
    def faulty_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)

    captured = capsys.readouterr()
    assert "faulty_function started" in captured.out
    assert "faulty_function Error:" in captured.out
    assert "Inputs: (1, 0)" in captured.out
    assert "faulty_function finished" in captured.out
