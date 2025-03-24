from typing import Union


# я решил перегрузить операцию суммы для чисел с плавающей точкой
def sum_operation(a: Union[int, float], b: Union[int, float]) -> Union[int, float, None]:
    if a is None or b is None:
        return None
    return a + b
