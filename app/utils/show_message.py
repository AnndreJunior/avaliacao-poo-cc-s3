from .clean import clean
from .next import next


def show_message(message) -> None:
    clean()
    print(message)
    next()
