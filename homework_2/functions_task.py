from homework_2 import SearchType


def _slow_search(target_number: int, finder_list: list[int]) -> tuple[int | None, int]:
    """
    Функция поиска числа в списке методом медленного перебора

    Args:
        target_number: Число, которое необходимо найти
        finder_list: Список целых чисел для поиска

    Returns:
        Кортеж:
            - Если число найдено: (число, количество сравнений)
            - Если число не найдено: (None, количество сравнений)
    """

    for i, value in enumerate(finder_list):
        if value == target_number:
            return value, i + 1
    return None, len(finder_list)


def _binary_search(target_number: int, finder_list: list[int]) -> tuple[int | None, int]:
    """
    Функция поиска числа в списке методом бинарного поиска

    Args:
        target_number: Число, которое необходимо найти
        finder_list: Список целых чисел для поиска

    Returns:
        Кортеж:
            - Если число найдено: (число, количество угадываний)
            - Если число не найдено: (None, количество угадываний)
    """

    counter = 0
    buffer_list = sorted(finder_list.copy())
    while len(buffer_list) > 0:
        counter += 1
        middle_index = len(buffer_list) // 2
        if buffer_list[middle_index] == target_number:
            return buffer_list[middle_index], counter
        elif buffer_list[middle_index] < target_number:
            buffer_list = buffer_list[middle_index + 1:]
        else:
            buffer_list = buffer_list[:middle_index]
    return None, counter


def guess_number(target_number: int, finder_list: list[int], search_type: SearchType) -> tuple[int | None, int]:
    """
    Функция поиска числа в списке указанным алгоритмом

    Args:
        target_number: Число, которое необходимо найти
        finder_list: Список целых чисел для поиска
        search_type: Тип алгоритма поиска из перечисления SearchType

    Returns:
        Кортеж:
            - Если число найдено: (число, количество сравнений)
            - Если число не найдено: (None, количество сравнений)

    Raises:
        ValueError: Если передан неподдерживаемый тип поиска
    """
    match search_type:
        case SearchType.SLOW_SEARCH:
            return _slow_search(target_number, finder_list)
        case SearchType.BINARY_SEARCH:
            return _binary_search(target_number, finder_list)
        case _:
            raise ValueError(f"Неправильный тип сортировки: '{search_type}'")


def helper():
    """
    Вспомогательная функция для ввода данных с клавиатуры.

    """

    print("/===== Угадай число =====\\")

    try:
        start_input = int(input("Введите минимальное значение диапазона: "))
        end_input = int(input("Введите максимальное значение диапазона: "))
        if start_input == end_input:
            print("Ошибка: начало диапазона должно быть равно концу диапазона")
            print("\\===== Угадай число =====/")
            return helper()
    except ValueError:
        print("Ошибка: ввод должен быть целочисленным")
        print("\\===== Угадай число =====/")
        return helper()

    numbers = list(range(start_input, end_input + 1)) \
        if start_input < end_input else list(range(start_input, end_input - 1, -1))

    try:
        target = int(input("Введите число для угадывания: "))

        if target not in numbers:
            print(f"Ошибка: число должно быть в диапазоне")
            print("\\===== Угадай число =====/")
            return helper()
    except ValueError:
        print("Ошибка: введите целое число")
        print("\\===== Угадай число =====/")
        return helper()

    method = input("Выберите метод (binary/linear): ").strip().lower()
    if method not in ["binary", "linear"]:
        print("Ошибка: метод должен быть 'binary' или 'linear'")
        print("\\===== Угадай число =====/")
        return helper()
    method = SearchType.BINARY_SEARCH if method == "binary" else SearchType.SLOW_SEARCH



    value, counter = guess_number(target, numbers, method)
    print("Результат:", f"\t - Значение: {value}", f"\t - Количество проходов: {counter}", sep="\n")

    print("\\===== Угадай число =====/")
    return None


if __name__ == '__main__':
    helper()
