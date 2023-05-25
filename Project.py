import random

def generate_sequence(length):
    sequence = [random.choice([0, 1]) for _ in range(length)]
    return sequence

def monobit_test(sequence):
    ones_count = sequence.count(1)
    zeros_count = sequence.count(0)
    if ones_count < 9654 or ones_count > 10346 or zeros_count < 9654 or zeros_count > 10346:
        return False
    return True


def max_length_test(sequence):
    max_ones_series = max_zeros_series = 0
    ones_series = zeros_series = 0
    prev_bit = None
    for bit in sequence:
        if bit == 1:
            ones_series += 1
            zeros_series = 0
            max_ones_series = max(max_ones_series, ones_series)
        else:
            zeros_series += 1
            ones_series = 0
            max_zeros_series = max(max_zeros_series, zeros_series)
        prev_bit = bit
    if max_ones_series > 36 or max_zeros_series > 36:
        return False
    return True


def generate_sequence(length):
    sequence = [random.choice([0, 1]) for _ in range(length)]
    return sequence


def pokker_test(sequence):
    m = 4  # Довжина блоку Поккера
    k = len(sequence) // m  # Кількість блоків Поккера

    def count_block_frequencies(sequence, block_length):
        frequencies = {}
        for i in range(len(sequence) - block_length + 1):
            block = tuple(sequence[i:i + block_length])
            if block in frequencies:
                frequencies[block] += 1
            else:
                frequencies[block] = 1
        return frequencies

    def calculate_expected_frequency(block_length, sequence_length):
        possible_blocks = 2 ** block_length
        return sequence_length / possible_blocks

    block_frequencies = count_block_frequencies(sequence, m)
    observed_frequencies = list(block_frequencies.values())
    expected_frequency = calculate_expected_frequency(m, len(sequence))

    X2 = sum((observed - expected_frequency) ** 2 / expected_frequency for observed in observed_frequencies)
    chi_square = 11.3449  

    if X2 < chi_square:
        return True
    return False



def length_test(sequence):
    series_ones = [0] * 6
    series_zeros = [0] * 6
    current_series = 0
    current_bit = None

    for bit in sequence:
        if bit == current_bit:
            current_series += 1
        else:
            if current_bit == 1:
                if current_series >= 6:
                    series_ones[5] += 1
                else:
                    series_ones[current_series - 1] += 1
            elif current_bit == 0:
                if current_series >= 6:
                    series_zeros[5] += 1
                else:
                    series_zeros[current_series - 1] += 1

            current_series = 1
            current_bit = bit

    if current_bit == 1:
        if current_series >= 6:
            series_ones[5] += 1
        else:
            series_ones[current_series - 1] += 1
    elif current_bit == 0:
        if current_series >= 6:
            series_zeros[5] += 1
        else:
            series_zeros[current_series - 1] += 1

    series_intervals = [(2267, 2733), (1079, 1421), (502, 748), (223, 402), (90, 223), (90, 223)]

    for i, (start, end) in enumerate(series_intervals):
        if series_ones[i] < start or series_ones[i] > end or series_zeros[i] < start or series_zeros[i] > end:
            return False

    return True


sequence = generate_sequence(20000)

series_length_result = length_test(sequence)
if series_length_result:
    print("Тест довжин серій пройдено.")
else:
    print("Тест довжин серій не пройдено.")

sequence = generate_sequence(20000)

monobit_result = monobit_test(sequence)
if monobit_result:
    print("Монобітний тест пройдено.")
else:
    print("Монобітний тест не пройдено.")

sequence = generate_sequence(20000)

max_length_result = max_length_test(sequence)
if max_length_result:
    print("Тест максимальної довжини серій пройдено.")
else:
    print("Тест максимальної довжини серій не пройдено.")

sequence = generate_sequence(20000)

pokker_result = pokker_test(sequence)
if pokker_result:
    print("Тест Поккера пройдено.")
else:
    print("Тест Поккера не пройдено.")
