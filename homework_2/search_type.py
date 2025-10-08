import enum


class SearchType(enum.Enum):
    """
    Перечисление для выбора алгоритма поиска

    Attributes:
        SLOW_SEARCH: Медленный перебор
        BINARY_SEARCH: Бинарный поиск
    """
    SLOW_SEARCH = "linear"
    BINARY_SEARCH = "binary"
