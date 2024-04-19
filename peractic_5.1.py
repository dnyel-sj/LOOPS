# برنامه شمارش اعداد مثبت و منفی و محاسبه مجموع و میانگین آنها

# تعریف متغیرها
positives = 0  # تعداد اعداد مثبت
negatives = 0  # تعداد اعداد منفی
count = 0  # تعداد کل اعداد
total = 0  # مجموع اعداد

# ورودی کاربر را دریافت می کند
number = int(input("Yek add sahih ra vared konid: "))

# بررسی خروج از برنامه
if number == 0:
    print("Add vared shode barabar 0 va tarif nashode ast!")
    exit(1)

# حلقه اصلی برنامه
while number != 0:

    # دریاف ورودی جدید از کاربر 
    number = int(input("Yek add sahih ra vared konid: "))

    # بررسی عدد مثبت بودن
    if number > 0:
        positives += 1
    # بررسی عدد منفی بودن
    else:
        negatives += 1

    # جمع آوری اعداد
    total += number
    
    # شمارش اعداد
    count += 1

    # محاسبه میانگین
    average = total / count

# نمایش نتایج
print(f"Tedad adad mosbat :{positives}")
print(f"Tedad adad manfi :{negatives}")
print(f"Majmo adad :{total}")
print(f"Meiangin adad :{average}")
