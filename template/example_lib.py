def hello_world(name: str) -> str:
    """
    Return greeting based on given name
    """
    if not name:
        return "Please introduce yourself :("
    return f"hello {name}"


def calculate_square(number: int) -> int:
    """
    Return square of given number
    """
    return number**2
