import random

x = random.randint(1, 50)
print(x)
for __ in range(15):
    y = int(input("請猜數字"))
    if x == y:
        print("猜對了")
    else:
        print("才錯了")
