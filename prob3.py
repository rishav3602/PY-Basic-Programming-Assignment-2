# 3.Write a Python program to display calendar?

import calendar

yy = int(input("Enter the year you want to check : "))
mm = int(input("Enter the month you want to check : "))

print(calendar.month(yy,mm))

