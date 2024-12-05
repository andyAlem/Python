from src.decorators import log

def test_decorator(capsys):
    """Тестируем на успешное выполнение функции
     и обработку исключений"""
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1,2)
    captured = capsys.readouterr()
    assert ("my_function is ok" in captured.out)

    try:
        my_function(2, "Test")
    except TypeError:
        captured = capsys.readouterr()
        assert (
                "my_function Error: unsupported operand type(s) for +: "
                "'int' and 'str'. Inputs: (0, 'Test'), {}" in captured.out)

