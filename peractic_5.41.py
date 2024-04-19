# برنامه بزرگ ترین عدد ورودی چاپ و تعداد تکرار ان را نشان میدهد 

# تعریف متغییر ها
bozorgtarin = 0
Tekrar = 1

# دریافت 7 عدد از کاربر
for i in range(7):
  Adad = eval(input("Yek adad ra vared konid: "))

  # مقایسه عدد با بزرگترین عدد فعلی
  if Adad > bozorgtarin:
    bozorgtarin = Adad

  elif Adad == bozorgtarin:
    Tekrar += 1

# نمایش نتیجه
print("Bozorgtarin adad mojod:",bozorgtarin)
print("Tedad tekrar adad:",Tekrar)
