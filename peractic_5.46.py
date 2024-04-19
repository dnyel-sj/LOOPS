# برنامه ای که با استفاده از فرمول های مربوطه میانگین اعداد و میزان انحراف معیار را محاسبه میکند 
  
# تعداد ورودی ها را مشخص می کنیم
Tedad_vorodi = 10

# متغیرهایی برای جمع مقادیر و میانگین
Majmo = 0
Meiangin = 0

# دریافت 10 ورودی از کاربر
for i in range(Tedad_vorodi):
  Vorodi = float(input(f"Vorodi ra vared konid: "))
  Majmo += Vorodi

# محاسبه میانگین
Meiangin = Majmo / Tedad_vorodi

# محاسبه اختلافات مجذور با میانگین
Ekhtelaf_majzor = 0
for i in range(Tedad_vorodi):
  Ekhtelaf = Vorodi - Meiangin
  Ekhtelaf_majzor += (Ekhtelaf ** 2)

# محاسبه انحراف معیار
Enheraf_meiar= (Ekhtelaf_majzor / Tedad_vorodi) ** 0.5

# نمایش نتایج
print(f"Meiangin :{Meiangin}")
print(f"Enheraf : {Enheraf_meiar}")
