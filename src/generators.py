from typing import Iterable


def card_number_generator(start: int, end: int) -> Iterable[str]:
    for num in range(start, end + 1):
        number = f"{'0' * (16 - len(str(num)))}{num}"
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"


def transaction_descriptions(transaction: list) -> Iterable:
    for desc in transaction:
        yield desc['description']


def get_id_transactions(transaction: list, currency: str = 'USD') -> Iterable:
    for i in transaction:
        if i['operationAmount']['currency']['code'] == currency:
            yield i


