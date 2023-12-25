import datetime

def decorator(func):
    cash = dict()

    def wrapper(num):
        if num not in cash:
            cash[num] = func(num)
        return cash[num]
    return wrapper


@decorator
def calc(num):
    return num ** num

start = datetime.datetime.now()
numbers = [1000, 200000, 312310, 43123, 50000, 1000, 200000, 3, 4, 312310, 43123, 312310, 43123, 312310, 43123,]
for number in numbers:
    (calc(number))
end = datetime.datetime.now()
print(end - start)
