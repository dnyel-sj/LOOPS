# بازی سنگ کاغذ و قیچی
import random

print("Welcom to game!")

while True:
  # انتخاب کاربر
  user_choice = input("Sang, Kaghaz, Gheychi yeki entekhab kn: ")

  # انتخاب کامپیوتر
  computer_choice = random.choice(["Sang", "Kaghaz", "Gheychi"])

  # نمایش انتخاب ها
  print(f"Shoma {user_choice} entekhab kardid.")
  print(f"PC {computer_choice} entekhab kard.")

  # تعیین برنده
  if user_choice == computer_choice:
    print("Mosavi!")
  elif computer_choice == "Kaghaz" and user_choice == "Gheychi":
    print("Gheychi kaghaz borid piroozi!")
  elif computer_choice == "Sang" and user_choice == "Kaghaz":
    print("Kaghaz sang khord piroozi!")
  elif computer_choice == "Gheychi" and user_choice == "Sang":
    print("Kaghaz sang khord piroozi!")
  elif user_choice == "Sang" and computer_choice == "Kaghaz":
    print("Kaghaz sang ghort dad pc bord!")
  elif user_choice == "Kaghaz" and computer_choice == "Gheychi":
    print("Gheychi kaghaz borid pc bord!")
  elif user_choice == "Gheychi" and computer_choice == "Sang":
    print("sang ghechi shekast pc bord!")
  else:
    print("Ba tashakor!")