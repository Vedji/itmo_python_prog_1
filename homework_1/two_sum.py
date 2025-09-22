from typing import Any


def valid_num(num: Any) -> int:
    """
    Валидация входного числа
    """

    if isinstance(num, str):
        if num.count('.') == 1 or num.count(',') == 1:
            buffer = float(num)
            if buffer.is_integer():
                return int(buffer)
        elif num.replace('-', '', 1).isdigit():
            return int(num)
    if isinstance(num, float) and num.is_integer():
        return int(num)
    if isinstance(num, int):
        return num
    raise TypeError(f'Неверный ввод, "{num}" должно быть целочисленным')


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Поиск суммы двух чисел в масиве
    """
    try:
        validated_target = valid_num(target)
        validated_nums = list(map(valid_num, nums))
    except TypeError:
        return None

    for i, i_num in enumerate(validated_nums):
        for j, j_nums in enumerate(validated_nums):
            if j == i:
                continue
            if i_num + j_nums == validated_target:
                return i, j

    return None
