# برنامه یافتن بهترین نمره دانش آموزان یک کلاس

# تعریف متغیرها
Tedad_daneshamozan= 0
Behtarin_nomre= 0

# دریافت تعداد دانش آموزان
while True:
  try:
    Tedad_daneshamozan = int(input("\nTedad daneshamozan vared konid: "))
    if Tedad_daneshamozan > 0:
      break
    else:
      print("Tedad bayad adadi mosbat bashad!")
  except ValueError:
    print("Tedad bayad adadi mosbat bashad!")

# دریافت نمرات دانش آموزان
for i in range(0, Tedad_daneshamozan):
  while True:
    try:
      Nomre = float(input(f"\nNomre daneshamozan ra vared konid: "))
      if 0 <= Nomre <= 20:
        break
      else:
        print("\nNomre bayad beyn 0 ta 20 bashad")
    except ValueError:
      print("Nomre bayad beyn 0 ta 20 bashad")

  # پیدا کردن بهترین نمره
  if Nomre > Behtarin_nomre:
    Behtarin_nomre = Nomre

# نمایش بهترین نمره
print(f"\nBehtarin nomre: {Behtarin_nomre}")
