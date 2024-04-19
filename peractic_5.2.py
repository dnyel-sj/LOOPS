# ایجاد 10 سوال جمع تصادفی و پاسخ از طرف کاربر و نشان دادن تعداد جواب صحیح و مدت زمان صرف شده توسط کاربر

import random
import time
 
# متغییر تعریف میکنیم
correct_count = 0
start_time = time.time()

# 10 سوال تولید می کنیم
for _ in range(10):
  # دو عدد تصادفی بین 1 و 15 ایجاد می کنیم
  num1 = random.randint(1, 15)
  num2 = random.randint(1, 15)

  # سوال و پاسخ را ایجاد می کنیم
  question = f"{num1} + {num2} = "
  answer = num1 + num2

  # سوال را چاپ می کنیم
  print(question)

  # پاسخ کاربر را دریافت می کنیم
  user_answer = int(input())

  # پاسخ را بررسی می کنیم
  if user_answer == answer:
     correct_count += 1
     print("Dorost!")
  else:
    print(f"Ghalat! pasokh dorost :{answer} ast.")

# زمان صرف شده را محاسبه می کنیم
end_time = time.time()
elapsed_time = end_time - start_time

# نتایج را چاپ می کنیم
print(f"\nShoma {correct_count} az 10 soal be dorosti javab dadid.")
print(f"Zaman sarf shode shoma :{elapsed_time:.2f} sanie ast.")
