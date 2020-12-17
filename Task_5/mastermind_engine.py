from random import randint

NUMBER = ''


def make_number():
    global NUMBER
    NUMBER = ''

    for i in range(4):
        while True:
            number_candidate = str(randint(0, 9))

            for j in NUMBER[0:i]:
                if j == number_candidate:
                    break   # выносит из for в while ниже (дальше)

            else:
                NUMBER += number_candidate
                break   # выносит и из for, и из while ниже (дальше)

    # print(NUMBER)
    # NUMBER = ''


def check_number(str_number):    # возвращает словарь {'bulls': N, 'cows': N}
    bulls = 0
    cows = 0

    for i in range(len(str_number)):
        for j in range(len(NUMBER)):
            if str_number[i:i+1] == NUMBER[j:j+1]:
                if i == j:
                    bulls += 1
                else:
                    cows += 1

    return {'Bulls: ': bulls, 'Cows: ': cows}


if __name__ == '__main__':
    # for _ in range(20):
    make_number()
    bc = check_number(input('Введите число: '))
    print(f'NUMBER = {NUMBER}, bc = {bc}')
