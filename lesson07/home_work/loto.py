#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random

#рандом из number_in_list значений в списке и до числа random_before
def random_list(number_in_list, random_before):
    card_list = []
    while len(card_list) < number_in_list:
        b = int(random.randint(1, random_before))
        if b not in card_list:
            card_list.append(b)
    return card_list

#создание списка из 9 уникальными рандомными значениями с пустыми строками
def create_list():
    #Позиция для пустых строк с уникальными значениями
    position1 = random.randint(0,8)
    position2 = random.randint(0,8)
    position3 = random.randint(0,8)
    position4 = random.randint(0,8)

    while position1 == position2:
        position2 = random.randint(0,8)
    while position1 == position3 or position2 == position3:
        position3 = random.randint(0,8)
    while position1 == position4 or position2 == position4 or position3 == position4:
        position4 = random.randint(0,8)
    #создание списка из 9 значений с пустыми строками
    newlist = [0] * 9

    newlist[position1] = " "
    newlist[position2] = " "
    newlist[position3] = " "
    newlist[position4] = " "

    return newlist
#добавление list1 - список из 5 уникальных рандомных символов к list2 - список с 9 значениями и пустыми строками, в незаполненные поля
def add_create_list(list1, list2):
    index_list1 = 0
    for n, i in enumerate(list2):
        if i == 0:
            list2[n] = list1[index_list1]
            index_list1 += 1

    return list2

def change_in_list(i, list):
    for n, j in enumerate(list):
        if j == i:
            list[n] = "-"
    return list

def check_winner(list1):
    winner = 0
    for i in list1:
        if i == "-":
            winner += 1
    return winner

if __name__ == '__main__':
    #рандом из 15 значений для карт человека и компьютера
    card_human = random_list(15, 90)
    card_comp = random_list(15, 90)

    #фишки (бочонки) с цифрами в рандомном порядке в виде списка
    box_list = random_list(90, 90)

    #отображение в виде 3 строк по 5 отсортированных значения
    card_human1 = sorted(card_human[0:5])
    card_human2 = sorted(card_human[5:10])
    card_human3 = sorted(card_human[10:15])

    card_comp1 = sorted(card_comp[0:5])
    card_comp2 = sorted(card_comp[5:10])
    card_comp3 = sorted(card_comp[10:15])

    #создание списков из 9 уникальными рандомными значениями с пустыми строками
    create_list_human1 = create_list()
    create_list_human2 = create_list()
    create_list_human3 = create_list()

    create_list_comp1 = create_list()
    create_list_comp2 = create_list()
    create_list_comp3 = create_list()

    #объединение списка с 5 значениями в список с 9 значениями и пустыми строками
    add_list_human1 = add_create_list(card_human1, create_list_human1)
    add_list_human2 = add_create_list(card_human2, create_list_human2)
    add_list_human3 = add_create_list(card_human3, create_list_human3)

    add_list_comp1 = add_create_list(card_comp1, create_list_comp1)
    add_list_comp2 = add_create_list(card_comp2, create_list_comp2)
    add_list_comp3 = add_create_list(card_comp3, create_list_comp3)

    exit = False



    print("\nЗдравствуйте, давайте сыграем в лото?")
    go = input('\nЧто бы играть введите "y": ')

    if go == "y":
        len_box_list = len(box_list)

        for i in box_list:
            len_box_list = len_box_list - 1 #определяем сколько бочонков осталось
            if check_winner(add_list_human1) + check_winner(add_list_human2) + check_winner(add_list_human3) == 15:
                print("Вы выиграли, поздравляем!\n")
                break

            if check_winner(add_list_comp1) + check_winner(add_list_comp2) + check_winner(add_list_comp3) == 15:
                print("К сожалению, Вы проиграли!\n")
                break

            print("\nНовый бочонок: " + str(i) + " (осталось " + str(len_box_list) + ")")

            print("------------ Ваша карточка -------------")
            print(add_list_human1)
            print(add_list_human2)
            print(add_list_human3)
            print("----------------------------------------")

            print("--------- Карточка компьютера ----------")
            print(add_list_comp1)
            print(add_list_comp2)
            print(add_list_comp3)
            print("----------------------------------------")
            #зачеркиваем цифры у человека
            add_list_human12 = add_list_human1.copy()
            add_list_human22 = add_list_human2.copy()
            add_list_human32 = add_list_human3.copy()

            change_last_human1  = change_in_list(i, add_list_human12)
            change_last_human2  = change_in_list(i, add_list_human22)
            change_last_human3  = change_in_list(i, add_list_human32)

            #зачеркиваем цифры у компа
            add_list_comp1  = change_in_list(i, add_list_comp1)
            add_list_comp2  = change_in_list(i, add_list_comp2)
            add_list_comp3  = change_in_list(i, add_list_comp3)

            cross_out = input("Зачеркнуть цифру? (y/n): ")
            #проверяем соотвествутет ли выбор человека правде

            if cross_out == "n":
                if i in add_list_human1 or i in add_list_human2 or i in add_list_human3:
                    print("\nТакая цифра есть, будьте внимательнее. Вы проиграли!")
                    break

            elif cross_out == "y":
                if change_last_human1 == add_list_human1 and change_last_human2 == add_list_human2 and change_last_human3 == add_list_human3:
                    print("\nТакой цифры нет, Вы проиграли!")
                    break
                else:
                    add_list_human1 = change_last_human1
                    add_list_human2 = change_last_human2
                    add_list_human3 = change_last_human3
