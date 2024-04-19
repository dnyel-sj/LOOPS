# حدس عدد توسط کاربر
import random

# ایجاد یک عدد رندوم تو بازه 0 تا 100
number = random.randint(0 , 100)

guess = -1
while guess != number:
    guess = eval(input("Yek add shansi entekhab kn: "))
    if guess == number:
        print("Awli, hadset dorost bod!")
    elif guess > number:
        print("Hadset bozorg tar az add ma ast!")
    else:
        print("Hadset kochek tar az add ma ast!")

