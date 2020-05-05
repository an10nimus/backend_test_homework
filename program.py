import datetime as dt

class Record:
    def __init__(self, amount, comment, date = dt.datetime.now()):
        self.amount = amount
        if isinstance(date, str):
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')
        else:
            self.date = date
        self.comment = comment

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    
    def add_record(self, new_record):
        self.records.append(new_record)
    
    def get_today_stats(self):
        tmp = 0
        for i in self.records:
            if i.date.date() == dt.datetime.now().date():
                tmp = tmp + i.amount
        return tmp
    
    def get_week_stats(self):
        tmp = 0
        for record in self.records:
            if (dt.datetime.now() - record.date).days < 7:
                tmp = tmp + record.amount
        return tmp
    
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        delta = self.limit - self.get_today_stats()
        if delta > 0:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {delta} кКал')
        else:
            print('Хватит есть!')

class CashCalculator(Calculator):    
    def get_today_cash_remained(self,currency):
        USD_RATE = 75.00
        EURO_RATE = 85.00
        currencies = {
        'rub' : [1, 'руб'],
        'usd' : [USD_RATE, 'USD'],
        'eur' : [EURO_RATE, 'Euro']
        }
        delta = self.limit - self.get_today_stats()
        if delta > 0:
            print(f'На сегодня осталось {delta/currencies[currency][0]:.2f} {currencies[currency][1]}')
        elif delta == 0:
            print('Денег нет, держись')
        else:
            print(f'Денег нет, держись: твой долг - {delta/currencies[currency][0]:.2f} {currencies[currency][1]}')
# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг", date="06.05.2020")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2020")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")
# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="01.05.2020")
r5 = Record(amount=84, comment="Йогурт.", date="02.05.2020")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="06.05.2020")
Cash = CashCalculator(10000)
Cash.add_record(r1)
Cash.add_record(r2)
Cash.add_record(r3)
Cash.get_today_cash_remained('usd')
Calories = CaloriesCalculator(10000)
Calories.add_record(r4)
Calories.add_record(r5)
Calories.add_record(r6)
Calories.get_calories_remained()
#Calories.get_today_stats()