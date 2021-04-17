# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# + Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# + Кот живет с человеком в доме.
# + Для кота дом характеризируется - миской для еды и грязью.
# + Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
# +  подобрать кота - у кота появляется дом.
# +  купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
# +  убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# + Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# + Когда кот спит - сытость уменьшается на 10
# + Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# + Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# + Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# + что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return f'Имя: {self.name}, Сытость: {self.fullness}'

    def enter_the_house(self, house):
        self.house = house
        print(f'{self.name} въехал в дом.')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} сегодня спал, сытости осталось: {self.fullness}')

    def eat(self):
        if self.house.food_for_cat >= 10:
            self.house.food_for_cat -= 10  # еда в доме уменьшается на 10
            self.fullness += 30
            print(f'{self.name} сегодня поел, теперь сытости: {self.fullness}, а кошачьей еды осталось: {self.house.food_for_cat}')
        else:
            self.fullness -= 10
            print(f'{self.name} сегодня не смог поесть, т.к. кошачьей еды осталось: {self.house.food_for_cat}. Теперь сытости: {self.fullness}')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5  # степень грязи в доме увеличивается на 5
        print(f'{self.name} сегодня драл обои, сытости осталось: {self.fullness}, а грязи в доме: {self.house.dirt}')

    def act(self):
        if self.fullness <= 0:
            print(f"Кот {self.name} умер от голода =(")
            return

        if self.fullness <= 50:
            self.eat()
            return

        dice = randint(1, 3)

        if dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.tear_wallpaper()
        else:
            print(f' --- Что делать, если выпало {dice} ? --- ')


class House:
    def __init__(self):
        self.money = 0
        self.food_for_man = 50
        self.food_for_cat = 0
        self.dirt = 0  # грязь (драные обои)

    def __str__(self):
        return f'В доме осталось: Денег: {self.money}, Еды: {self.food_for_man}, Еды для кота: {self.food_for_cat}, ' \
               f'Грязи: {self.dirt}'


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Имя: {self.name}, Сытость: {self.fullness}'

    def enter_the_house(self, house):
        self.house = house
        print(f'{self.name} въехал в дом. {house}')

    def ready_to_new_cat(self, i):
        if self.house.money >= 100 and self.house.food_for_cat > 100 and self.house.dirt < 200:
            return True
        else:
            return False

    def enter_the_house_cat(self, cat):
        cat.enter_the_house(self.house)
        # cat.house = self.house

    def buy_food_for_man(self):
        if self.house.money >= 100:
            self.house.money -= 100
            self.house.food_for_man += 50
            print(f'{self.name} Купил человеческую еду, теперь её: {self.house.food_for_man}, осталось денег: {self.house.money}')
        else:
            print(f'{self.name} не смог купить человеческую еду, т.к. денег осталось: {self.house.money}')
            self.go_work()

    def buy_food_for_cat(self):
        if self.house.money >= 100:
            self.house.money -= 100
            self.house.food_for_cat += 100
            print(f'{self.name} Купил еду для кота, теперь её: {self.house.food_for_cat}, осталось денег: {self.house.money}')
        else:
            print(f'{self.name} не смог купить еду для кота, т.к. денег осталось: {self.house.money}')
            self.go_work()

    def clean_house(self):
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0
        self.fullness -= 20
        print(f'{self.name} убрался в доме, теперь грязи: {self.house.dirt}, а сытости осталось: {self.fullness}')

    def go_work(self):
        self.house.money += 150
        self.fullness -= 30
        print(f'{self.name} сходил на работу, теперь денег: {self.house.money}, а сытости осталось: {self.fullness}')

    def rest(self):
        self.fullness -= 10
        print(f'{self.name} сегодня отдыхал, сытости осталось: {self.fullness}')

    def eat(self):
        if self.house.food_for_man >= 10:
            self.house.food_for_man -= 10
            self.fullness += 50
            print(f'{self.name} сегодня поел, теперь сытости: {self.fullness}, еды осталось: {self.house.food_for_man}')
        else:
            print(f'{self.name} не смог поесть, т.к. еда кончилась ! =О')
            self.buy_food_for_man()

    def act(self):
        if self.fullness <= 0:
            print(f"Человек {self.name} умер от голода х_Х")
            return

        if self.fullness <= 50:
            self.eat()
            return

        if self.house.food_for_man <= 10:
            self.buy_food_for_man()
            return

        if self.house.food_for_cat <= 10:
            self.buy_food_for_cat()
            return

        if self.house.money <= 150:
            self.go_work()
            return

        if self.house.dirt >= 200:
            self.clean_house()
            return

        dice = randint(1, 6)

        if dice == 1:
            self.buy_food_for_man()
        elif dice == 2:
            self.buy_food_for_cat()
        elif dice == 3:
            self.clean_house()
        elif dice == 4:
            self.go_work()
        elif dice == 5:
            self.rest()
        elif dice == 6:
            self.eat()
        else:
            print(f' --- Что делать, если выпало {dice} ? --- ')


####################################

mans = [
    Man("Вова"),
]

# Vova = Man("Вова")
Home = House()
# Murzik = Cat("Мурзик")

cats = [
    Cat("Мурзик"),
]

mans[0].enter_the_house(Home)
mans[0].enter_the_house_cat(cats[0])

for i in range(1, 366):
    print(f'================ День {i} - Начало ================')
    for man in mans:
        man.act()
        if man.ready_to_new_cat(i):
            cats.append(Cat("Мурзик"+str(i)))
            man.enter_the_house_cat(cats[len(cats) - 1])
    for cat in cats[::-1]:
        cat.act()
    print(f'---------------- День {i} - Завершение ------------')

# Vova.enter_the_house(Home)
# Vova.enter_the_house_cat(Murzik)
# Vova.buy_food_for_man()
# Vova.buy_food_for_cat()
# Vova.clean_house()
# Vova.go_work()
# Vova.rest()
# Vova.eat()
#
# # Murzik.enter_the_house(Home) # это человек должен принести его в дом
# Murzik.sleep()
# Murzik.eat()
# Murzik.tear_wallpaper()
# Murzik.act()
