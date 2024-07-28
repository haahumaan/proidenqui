from typing import overload

@overload
def my_function(a: int) -> str:
    ...

@overload
def my_function(a: str) -> bool:
    ...

def my_function(a):
    if isinstance(a, int):
        return str(a)
    elif isinstance(a, str):
        return bool(a)
    else:
        raise TypeError
