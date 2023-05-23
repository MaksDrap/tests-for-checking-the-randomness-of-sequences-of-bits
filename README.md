Цей код виконує тести для перевірки випадковості послідовностей бітів. Функції:

1. `generate_sequence(length)`: Генерує випадкову послідовність бітів заданої довжини `length`.

2. `monobit_test(sequence)`: Виконує монобітний тест для переданої послідовності `sequence`. Цей тест перевіряє, чи є кількість одиниць та нулів у послідовності приблизно однаковою.

3. `max_length_test(sequence)`: Виконує тест максимальної довжини серій для переданої послідовності `sequence`. Тест перевіряє, чи не містить послідовність занадто довгих серій одиниць або нулів.

4. `pokker_test(sequence)`: Виконує тест Поккера для переданої послідовності `sequence`. Тест оцінює рівномірність розподілу підпослідовностей довжиною 4 у послідовності.

5. `length_test(sequence)`: Виконує тест довжин серій для переданої послідовності `sequence`. Тест перевіряє, чи не містить послідовність занадто багато серій однакових бітів однієї довжини.

У коді створюються послідовності бітів різної довжини (20000 бітів) та виконується кожен тест для цих послідовностей. Результати тестів виводяться на екран.
