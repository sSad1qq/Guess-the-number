import random


def is_valid(num):
    if str(num).isdigit() and 1 <= int(num) <= bord:
        return True
    return False


def continue_game():
    while True:
        print('Хотели бы сыграть еще разок? (y / n)')
        user_ans = str(input())
        if user_ans.lower() == 'y':
            game()
        elif user_ans.lower() == 'n':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


def input_num():
    while True:
        user_num = str(input())
        if is_valid(user_num):
            return user_num
        else:
            print(f'Может введем все-таки целое число от 1 до {bord}?')


def game():
    num_random = random.randint(1, bord)
    print(f'Введите число от 1 до {bord}')
    count_attempt = 0
    while True:
        user_num = int(input_num())
        count_attempt += 1
        if user_num == num_random:
            print(f'Вы угадали за {count_attempt} попыток, поздравляем!')
            continue_game()
            break
        elif user_num > num_random:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif user_num < num_random:
            print('Ваше число меньше загаданного, попробуйте еще разок')


print('Добро пожаловать в угадайку')
print('Задайте правую границу для случайного числа:')
bord = int(input())
game()