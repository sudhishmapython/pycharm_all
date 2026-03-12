# math module
import math
import statistics
import random
import datetime

x = math.sqrt(64)
y = math.floor(1.4)
a = math.pi
# print(a)
z = 5
# print('The factorial of', z, 'is:', math.factorial(z))

# print(statistics.mean([5,10]))
# print(statistics.median([1, 3, 2, 7,9,4,8]))
# print(statistics.mode([1, 11, 2, -5, 7, -9, 11]))
# print(statistics.mode(['red', 'green', 'blue', 'red']))
#
# coin_side = random.choice(['H','T'])
# print(coin_side)

items = [1, 2, 3, 4]
# random.shuffle(items)
# print(items)

# print(random.randrange(1,11))
# print(random.uniform(1, 5))
# print(random.randint(1, 6))

today = datetime.date.today()
# print(today)
d = datetime.date(2025, 12, 25)
# print(d)
# dt = datetime.datetime(2025, 12, 25, 15, 30)
# print(dt)
now = datetime.datetime.now()
# print(now)
formatted = now.strftime("%m-%Y-%d %H:%M:%S")
# print(formatted)