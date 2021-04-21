# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

# ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirt = 0   # грязь
        self.earn_money = 0     # счётчик заработанных денег за год
        self.bought_coat = 0    # счётчик купленных шуб за год

    def __str__(self):
        return f'Дом: Еды: {self.food}, Денег: {self.money}, Грязи: {self.dirt}'


class Man:  # человек (от него наследуются Husband и Wife)

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.eated = 0  # счётчик съеденной еды за год

    def __str__(self):
        return f'Имя: {self.name}, Сытость: {self.fullness}, Счастье: {self.happiness}'

    def enter_the_house(self, house):
        self.house = house
        cprint(f'{self.name} въехал в дом. {house}', color='cyan')

    def eat(self):
        if self.house.food >= 30:
            food_change = 30
        else:
            food_change = self.house.food

        self.house.food -= food_change
        self.fullness += food_change
        self.eated += food_change

        cprint(f'{self.name} поел(-а), сытость: {self.fullness}, осталось еды: {self.house.food}', color='grey')


class Husband(Man):

    # def __str__(self):
    #     return super().__str__()

    # def eat(self):
    #     super().eat()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        self.house.earn_money += 150
        cprint(f'{self.name} сходил на работу, теперь денег в доме: {self.house.money}', color='grey')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint(f'{self.name} играл, теперь счастья: {self.happiness}', color='grey')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода =(', color='grey', on_color='on_red')
            return
        if self.happiness <= 0:
            cprint(f'{self.name} умер от депрессии =(', color='grey', on_color='on_white')
            return

        if self.fullness <= 30:
            self.eat()
        elif self.house.money <= 120:
            self.work()
        elif self.happiness <= 30:
            self.gaming()
        else:
            rand_num = randint(1, 3)
            if rand_num == 1:
                self.eat()
            if rand_num == 2:
                self.work()
            if rand_num == 3:
                self.gaming()


class Wife(Man):

    # def __str__(self):
    #     return super().__str__()

    def shopping(self):
        self.fullness -= 10

        if self.house.money >= 120:
            food_count = 120
        else:
            food_count = self.house.money

        self.house.money -= food_count
        self.house.food += food_count

        cprint(f'{self.name} купила еду: {food_count}, теперь еды: {self.house.food}, осталось денег: {self.house.money}', color='grey')

    def buy_fur_coat(self):
        self.fullness -= 10

        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.house.bought_coat += 1
            cprint(f"{self.name} купила шубу. Осталось денег: {self.house.money}, счастья: {self.happiness}", color='grey')
        else:
            cprint("Не достаточно денег для покупки шубы !", color='red')

    def clean_house(self):
        self.fullness -= 10

        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0

        cprint(f"{self.name} убралась в доме. Теперь грязи: {self.house.dirt}", color="grey")

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умерла от голода =(', color='grey', on_color='on_red')
            return
        if self.happiness <= 0:
            cprint(f'{self.name} умерла от депрессии =(', color='grey', on_color='on_white')
            return

        if self.fullness <= 30:
            self.eat()
        elif self.house.food <= 60:
            self.shopping()
        elif self.happiness <= 30:
            self.buy_fur_coat()
        elif self.house.dirt >= 90:
            self.clean_house()
        else:
            rand_num = randint(1, 4)
            if rand_num == 1:
                self.eat()
            if rand_num == 2:
                self.shopping()
            if rand_num == 3:
                self.buy_fur_coat()
            if rand_num == 4:
                self.clean_house()


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

serge.enter_the_house(home)
masha.enter_the_house(home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()

    home.dirt += 5

    if home.dirt >= 90:
        serge.happiness -= 10
        masha.happiness -= 10

    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

cprint(f'\nИтог: Муж съел: {serge.eated}, Жена съела: {masha.eated}, Заработано денег: {home.earn_money}, Куплено шуб: {home.bought_coat}', color='green')

# TODO после реализации первой части - отдать на проверку учителю

# ####################################################### Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


# ####################################################### Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


# ####################################################### Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
