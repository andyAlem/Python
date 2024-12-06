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



