"""
Точка входа программы, инициирует параметры и запускает симплекс-метод.
"""

from simplexsus.simplexsus import simplexsus, to_dual_task

def main():
    """
    Точка входа программы - инициализация значений и вызов симплекс-метода.
    """
    minimize = False                            # Необходимость минимизации
    c = [-4, -18, -30, -5]                      # Коэффициенты целевой функции
    A = [[3, 1, -4, -1], [-2, -4, -1, 1]]       # Ограничения
    b = [-3, -3]                                # Правая часть ограничений
    f = 0

    c, A, b, minimize = to_dual_task(c, A, b, minimize)
    print("[ + ] Ans:", simplexsus(minimize, c, A, b, f))

    return 0


if __name__ == "__main__":
    main()
