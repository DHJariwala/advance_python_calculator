from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> None:
        self.a = a
        self.b = b
        self.operation = operation