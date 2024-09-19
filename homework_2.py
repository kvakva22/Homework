import random


def get_numbers_ticket(min, max, quantity):
    lotterylist = []

    if min < 1 or max > 1000:
        print("Числа повинні знаходитись у діапазоні від 1 до 1000")
        return lotterylist
    
    if min > max:
        print ("Мінімальне значення більше максимального. Будь ласка, перевірте введені дані!")
        return lotterylist
    
    try:
        number=random.sample(range(min, max), k=quantity)
        lotterylist=number
    except  ValueError:
        print(f"Неможливо обрати {quantity} значень з діапазону від {min} до {max}")
    return lotterylist


print(get_numbers_ticket(1,49,6))
