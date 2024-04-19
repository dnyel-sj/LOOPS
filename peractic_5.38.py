# یک برنامه ثانیه شمار ساده

#وارد کردن ماژور زمان
import time

# گرفتن ورودی زمان به ثانیه و شمارش اعداد 
seconds = int(input("Tedad sanie haye mored nazar ra vared kn: "))

while seconds > 0:
  print(f"\n{seconds} Sanie baghi mande")
  time.sleep(1)
  seconds -= 1

print("\nZaman be payan resid!")
