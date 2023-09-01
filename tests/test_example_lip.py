from template.example_lib import calculate_square, hello_world


def test_hello_world():
    assert hello_world("world") == "hello world"
    assert hello_world("") == "Please introduce yourself :("
    assert hello_world(" ") == "hello  "


def test_calculate_square():
    assert calculate_square(2) == 4
    assert calculate_square(0) == 0
    assert calculate_square(-1) == 1
    assert calculate_square(1) == 1
