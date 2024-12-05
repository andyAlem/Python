from src.decorators import log

def test_my_function(capsys):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1,2)
    captured = capsys.readouterr()
    assert ("my_function is ok" in captured.out)