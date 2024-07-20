import random

x = random.randint(1, 50)
print(x)
for i in range(15):
    y = int(input("請猜數字"))
    if x == y:
        print(f"猜對了,猜了{i+1}次")
        break
    else:
        if x > y:
            print("猜高點")
        else:
            print("猜低點")
if x != y:
    print(f"答案為{x},猜了{i+1}次")
