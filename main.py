import os
clear = lambda: os.system('cls') # Очистка консоли

# Красивый вывод матрицы
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print('')

# Выводит матрицу, как "исходную"
def print_input_matrix(input_matrix):
    clear()
    print("Исходная матрица:")
    print_matrix(input_matrix)

# Сугубо красивое округление
def round_to_good(num):
    return round(num) if round(num) == num else round(num * 10.0) / 10.0

# Проверка на линейную зависимость
def has_linear_dependence(matrix):
    rows, columns = len(matrix), len(matrix[0])
    
    for row in matrix:
        # Состоит ли вся строка из нулей
        if all(val == 0 for val in row[:-1]):
            return True

    return False

# Копирование матрицы
def copy_matrix(matrix):
    return [row[:] for row in matrix]

# Поиск оптимального индекса разрешающего элемента
def find_l(matrix, index):

    # Сбор индексов уже используемых элементов
    indexs_already_in_use = []
    for i in range(index):
        previous_column = copy_matrix(matrix)
        for j in range(0, len(matrix)):
            if previous_column[j] == 1 and not j in indexs_already_in_use:
                indexs_already_in_use.append(j)

    # Поиск оптимального элемента
    column = copy_matrix(matrix)
    for i in range(0, len(column)):
        if not i in indexs_already_in_use and column[i] == 1:
            return i
    
    # Если не нашёлся оптимальный элемент, выбираем любой
    for i in range(0, len(column)):
        if not i in indexs_already_in_use:
            return i

def find_solution(input_matrix):
    # Копирование исходной матрицы
    matrix = copy_matrix(input_matrix)
    rows, columns = len(matrix), len(matrix[0])

    for iteration in range(rows):
        # Новая матрица. Будущий результат итерации
        matrix_new = copy_matrix(matrix)

        # Индекс разрешающей строки
        l = find_l(matrix, iteration)

        if matrix[l][iteration] == 0:
            print_input_matrix(input_matrix)
            print("Система не имеет решений")
            return

        print(f'Оптимальный элемент на {l + 1} строке')
        
        # Индекс разрешающего столбца
        s = iteration

        # Деление разрешающей строки
        for j in range(iteration, columns):
            matrix_new[l][j] = round_to_good(matrix[l][j] / matrix[l][s])
        
        # Приведение разрешающего столбца к виду
        for i in range(rows):
            if i == l:
                continue
            matrix_new[i][s] = 0
        
        for i in range(rows):

            # Пропуск разрешающей строки
            if i == l:
                continue
            
            # Операции с другими элементами
            for j in range(s + 1, columns):
                matrix_new[i][j] = round_to_good(matrix[i][j] - matrix[l][j] * matrix[i][s] / matrix[l][s])
            
        # Применение новой матрицы к текущей
        matrix = copy_matrix(matrix_new)
        
        print(f'{iteration + 1} итерация')
        print_matrix(matrix_new)

    if has_linear_dependence(matrix):
        print_input_matrix(input_matrix)
        print("Система имеет линейную зависимость. Существует бесконечное количество решений")
    else:
        print("Система имеет единственное решение")

def main():
    # Ответ [3, 1, 2]
    matrix = [
        [2, -1, 1, 3],
        [1, 3, -2, 1],
        [0, 1, 2, 8]
    ]

    # Ответ [0.4, 0.9, 0.3]
    # matrix = [
    #     [1, 2, 3, 3],
    #     [2, 3, 2, 4],
    #     [3, 3, 4, 5]
    # ]

    # Нет решений
    # matrix = [
    #     [5, 12, 19, 25, 25],
    #     [10, 22, 16, 39, 25],
    #     [5, 12, 3, 25, 30],
    #     [20, 46, 34, 89, 70]
    # ]

    # Линейная зависимость
    # matrix = [
    #     [1, 2, 3, 4, 1],
    #     [5, 13, 13, 5, 3],
    #     [1, 5, 3, 1, 7],
    #     [3, 7, 7, 2, 12],
    #     [4, 5, 6, 1, 19]
    # ]

    print_input_matrix(matrix)
    find_solution(matrix)

if __name__ == "__main__":
    main()