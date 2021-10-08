from typing import Type, TypeVar

T = TypeVar('T')


def convert(object, type: Type[T]) -> T:
    return type(object)
