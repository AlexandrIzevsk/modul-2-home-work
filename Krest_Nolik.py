# ===================================================
#           Домашнее задание: Игра Крестики-Нолики
# ===================================================

# 1 Создание матрицы game_f[]
game_f = [
    [" ",0, 1, 2],
    [0, "-", "-", "-"],
    [1, "-", "-", "-"],
    [2, "-", "-", "-"]
]
# Введение имен игроков
user_name = [input('Введите имя игрока:') for i in range(2)]
print(f'Имя первого игрока-{user_name[0]}, имя второго игрока-{user_name[1]}')

# Декоратор - добавляет выбор клетки игроком и проверку корректности ввода
def commun_user(fn):
    def wrapper(i_j, user):

        count = 0
        # Ввод номер строки клетки и проверка корректности ввода
        # Цикл - три попытки корректного ввода номера строки
        for i in range(3):
            i_j_0 = input('Введите номер строки клетки:')
            if i_j_0 == '':
                print('Введенный номер строки(столбца) должен быть от 0 до 2')
                count += 1
            elif all(map(str.isdigit, i_j_0)):
                i_j_0 = int(i_j_0)
                if i_j_0 > 0 and i_j_0 <= 2:
                    i_j.append(i_j_0)
                    break
                elif i_j_0 == 0:
                    i_j.append(int(0))
                    break
                elif i_j_0 > 2:
                    print('Введенный номер строки(столбца) должен быть от 0 до 2')
                    count += 1
            else:
                print('Введеный номер строки(столбца) должен содержать цифры от 0 до 2')
                count +=1
        if count == 3:
            exit(1)

        # Ввод номер столбца клетки и проверка корректности ввода
        # Цикл - три попытки корректного ввода номера столбца
        for i in range(3):
            i_j_0 = input('Введите номер столбца клетки:')
            if i_j_0 == '':
                print('Введенный номер строки(столбца) должен быть от 0 до 2')
                count += 1
            elif all(map(str.isdigit, i_j_0)):
                i_j_0 = int(i_j_0)
                if i_j_0 > 0 and i_j_0 <= 2:
                    i_j.append(i_j_0)
                    break
                elif i_j_0 == 0:
                    i_j.append(int(0))
                    break
                elif i_j_0 > 2:
                    print('Введенный номер строки(столбца) должен быть от 0 до 2')
                    count += 1
            else:
                print('Введеный номер строки(столбца) должен содержать цифры от 0 до 2')
                count +=1
        if count == 3:
            exit(1)
        # Функция замены символа в матрицы игорового поля
        fn(i_j, user)
    return wrapper

# Функция заменяет элемент матрицы игрового поля
@commun_user
def chang_elem(i_j, user):
    global error_user # переменная для выполнения повтора ввода при указании клетки которая уже занята
    error_user = 0
    for coount_row, row in enumerate(game_f):
        for index, item in enumerate(row):
            if error_user == 2:
                break
            elif all([user == 1,
                    coount_row - 1 == i_j[0],
                    index - 1 == i_j[1],
                    item != "X",
                    item != "O"]):
                row[index] = str("X")
            elif all([user == 2,
                    coount_row - 1 == i_j[0],
                    index - 1 == i_j[1],
                    item != "X",
                    item != "O"]):
                row[index] = str("O")
            elif all([coount_row - 1 == i_j[0],
                    index - 1 == i_j[1],
                    item == "O" or item == "X"]):
                print()
                print(f'{i_j} Клетка занята')
                error_user = 2
                break
            print(row[index], end=" ")
        coount_row += 1
        print()


for row in game_f:
    for index, item in enumerate(row):
        print(row[index], end=" ")
    print()

for i in range(5):
    # Ход первого игрока
    count_1 = 0       # Переменная для подсчета числа попыток выбора пустой клетки игрового поля
    while True:
        count_1 += 1
        print(f'Ходит игрок - {user_name[0]}')
        user = 1      # Индефикатор игрока для определения симовола "Х" или "О" для установки в поле
        i_j = []      # переменная (список), которая будет содержать номер строки и столбца выбронной клетки
        chang_elem(i_j, user)      # Декорированная функция
        # Условие победы первого игрока
        if any([(game_f[1][1] == 'X') and (game_f[1][2] == 'X') and (game_f[1][3] == 'X'),
                (game_f[2][1] == 'X') and (game_f[2][2] == 'X') and (game_f[2][3] == 'X'),
                (game_f[3][1] == 'X') and (game_f[3][2] == 'X') and (game_f[3][3] == 'X'),
                (game_f[1][1] == 'X') and (game_f[2][1] == 'X') and (game_f[3][1] == 'X'),
                (game_f[1][2] == 'X') and (game_f[2][2] == 'X') and (game_f[3][2] == 'X'),
                (game_f[1][3] == 'X') and (game_f[2][3] == 'X') and (game_f[3][3] == 'X'),
                (game_f[1][1] == 'X') and (game_f[2][2] == 'X') and (game_f[3][3] == 'X'),
                (game_f[1][3] == 'X') and (game_f[2][2] == 'X') and (game_f[3][1] == 'X'), ]):
            print(f'Победил игрок {user_name[0]}. Поздравляю!!!')
            exit(1)
        # Условие ничьи
        elif all([(game_f[1][1] != '-') and (game_f[1][2] != '-') and (game_f[1][3] != '-'),
                (game_f[2][1] != '-') and (game_f[2][2] != '-') and (game_f[2][3] != '-'),
                (game_f[3][1] != '-') and (game_f[3][2] != '-') and (game_f[3][3] != '-')]):
            print(f'Победила дружба!')
            exit(1)
        # условие повтора при выборе клетки которая уже занята
        elif error_user == 0:
            break
        # условие завершения игры при трех неправильных попытках ввода клетки
        elif count_1 == 3:
            print(f'Игра завершена. Игрок {user_name[0]} три раза ввел занятую клетку')
            exit(1)

    # Ход второго игрока
    count_2 = 0       # Переменная для подсчета числа попыток выбора пустой клетки игрового поля
    while True:
        count_2 += 1
        print(f'Ходит игрок - {user_name[1]}')
        user = 2      # Индефикатор игрока для определения симовола "Х" или "О" для установки в поле
        i_j = []      # переменная (список), которая будет содержать номер строки и столбца выбронной клетки
        chang_elem(i_j, user)      # Декорированная функция
        # Условие победы первого игрока
        if any([(game_f[1][1] == 'O') and (game_f[1][2] == 'O') and (game_f[1][3] == 'O'),
                (game_f[2][1] == 'O') and (game_f[2][2] == 'O') and (game_f[2][3] == 'O'),
                (game_f[3][1] == 'O') and (game_f[3][2] == 'O') and (game_f[3][3] == 'O'),
                (game_f[1][1] == 'O') and (game_f[2][1] == 'O') and (game_f[3][1] == 'O'),
                (game_f[1][2] == 'O') and (game_f[2][2] == 'O') and (game_f[3][2] == 'O'),
                (game_f[1][3] == 'O') and (game_f[2][3] == 'O') and (game_f[3][3] == 'O'),
                (game_f[1][1] == 'O') and (game_f[2][2] == 'O') and (game_f[3][3] == 'O'),
                (game_f[1][3] == 'O') and (game_f[2][2] == 'O') and (game_f[3][1] == 'O'), ]):
            print(f'Победил игрок {user_name[1]}. Поздравляю!!!')
            exit(1)
        # Условие ничьи
        elif all([(game_f[1][1] != '-') and (game_f[1][2] != '-') and (game_f[1][3] != '-'),
                (game_f[2][1] != '-') and (game_f[2][2] != '-') and (game_f[2][3] != '-'),
                (game_f[3][1] != '-') and (game_f[3][2] != '-') and (game_f[3][3] != '-')]):
            print(f'Победила дружба!')
            exit(1)
        # условие повтора при выборе клетки которая уже занята
        elif error_user == 0:
            break
        # условие завершения игры при трех неправильных попытках ввода клетки
        elif count_2 == 3:
            print(f'Игра завершена. Игрок {user_name[1]} три раза ввел занятую клетку')
            exit(1)