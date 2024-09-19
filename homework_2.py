import random
def get_numbers_ticket(min, max, quantity):
    lotterylist = []
    if min < 1:
        print(lotterylist)
    if max > 1000:
        print(lotterylist)
    for number in range(quantity):
        number=random.sample(range(min, max), k=1)
        lotterylist=number
    return lotterylist

print(get_numbers_ticket(4,19,4))
