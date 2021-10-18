#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = tuple(map(int, input("Введите 10 чисел: ").split()))
    C = int(input("C = "))
    t = 0
    for i in a:
        if i > C:
            t += 1
    answ = 1
    for i in a[a.index(max(a)) + 1:]:
        answ *= i
    print("Количество элементов больших С: ", t)
    print("Произведение элементов,  расположенных после максимального элемента: ", answ)
    print("Отсортированный список: ", sorted(a))
