"""
Часто при зачислении каких-то средств на счет с нас берут комиссию. Давайте реализуем похожий механизм с помощью дескрипторов. Напишите дескриптор Value, который будет использоваться в нашем классе Account.
class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
        У аккаунта будет атрибут commission. Именно эту коммиссию и нужно вычитать при присваивании значений в amount.

new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)
90
"""


class Value:
    def __get__(self, instance, owner):  # что будет выводиться при запросе к ammount
        return self.result

    def __set__(self, instance,
                value):  # что будет происходить если мы приравняем атрибут к чему-то, на вход принимается
        self.result = value * (1 - instance.commission)  # класс атрибута и значение к которому мы приравниваем


class Account:
    def __init__(self, commission):
        self.commission = commission

    amount = Value()  # создаем атрибут класса который мы будем вычислять в дескрипторе Value


new_account = Account(0.3)  # создаём объект класса аккаунт и вводим комиссиб
new_account.amount = 100  # приравниваем атрибут объекта new_account класса Acount к какому-то значению
print(new_account.amount)  # значение изменится т.к будет работать дескриптор value и его метод set
new_account.amount = 160  # повтор что точно всё хорошо работает
print(new_account.amount)
