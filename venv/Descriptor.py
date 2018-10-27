class Value:
    def __get__(self, instance, owner):                             #принимаем данные из класса Аккаунт
        return instance.commission
    def __set__(self, instance, value):                             #устанавливаем ammount, которые мы задесриптировали в 10
        instance.commission = value * (1 - instance.commission)     # строке как ammount с учетом комиссии

class Account:
    def __init__(self, commission):
        self.commission = commission
    amount = Value()                                                #создаем атрибут класса который мы будем вычислять в value


new_account = Account(0.1)                                          #тут вводим комиссию
new_account.amount=100                                              #тут вводим amount который надо вычислить
print(new_account.amount)
