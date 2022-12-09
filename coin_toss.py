import random

coin = random.randint(0, 1)

if coin == 0:
    print(f"{coin} : Tails")
else:
    print(f"{coin} : Heads")