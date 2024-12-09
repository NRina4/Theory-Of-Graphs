def to_bit_scale(numbers, universe_size):
    """ Преобразует множество чисел в битовую шкалу. """
    bit_scale = 0
    for num in numbers:
        if 0 <= num < universe_size:
            bit_scale |= (1 << num)
        else:
            raise ValueError(f"Число {num} выходит за пределы [0, {universe_size - 1}]")
    return bit_scale


def union(bit_scale1, bit_scale2):
    """ Объединение двух множеств (битовых шкал). """
    return bit_scale1 | bit_scale2


def intersection(bit_scale1, bit_scale2):
    """ Пересечение двух множеств (битовых шкал). """
    return bit_scale1 & bit_scale2


def complement(bit_scale, universe_size):
    """ Дополнение множества относительно универсального множества. """
    full_set = (1 << universe_size) - 1  # Все элементы универсального множества
    return full_set - bit_scale


def difference(bit_scale1, bit_scale2):
    """ Разность двух множеств (битовых шкал). """
    return bit_scale1 - (bit_scale1 & bit_scale2)


def from_bit_scale(bit_scale):
    """ Преобразует битовую шкалу обратно в множество чисел. """
    return {i for i in range(bit_scale.bit_length()) if bit_scale & (1 << i)}


def display_bit_scale(bit_scale, universe_size):
    """ Отображает битовую шкалу в бинарном виде. """
    return bin(bit_scale)[2:].zfill(universe_size)


def generate_subset_codes(n):
    """ Генерирует последовательность кодов подмножеств для n-элементного множества. """
    for i in range(1 << n):  # range(0, 2^n)
        yield i


def Q(i):
    q = 1
    j = i
    while j % 2 == 0:
        j = j // 2
        q += 1
    return q


def generate_subsets_gray_code(n):
    """ Генерирует все подмножества n-элементного множества с использованием бинарного кода Грея. """
    B = [0] * n
    yield B

    for i in range(1, 1 << n):  # От 1 до 2^n - 1
        p = Q(i) - 1  # Индексы начинаются с 0, поэтому уменьшаем на 1
        B[p] = 1 - B[p]
        yield B
