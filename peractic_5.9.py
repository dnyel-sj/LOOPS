# محاسبه شهریه دانشگاه برای 4 سال و محاسبه تا 10 سال اینده

# شهریه سال اول
tuition_year_1 = 10000

# نرخ افزایش سالانه به درصد
annual_increase = 5

# تعداد سال ها
number_of_years = 10

# شهریه سال های آینده
for year in range(1, number_of_years + 1):
  tuition_year = tuition_year_1 * (1 + annual_increase / 100) ** (year)
  print(f"Shahrie sal {year}: {tuition_year:.2f}$")
  

