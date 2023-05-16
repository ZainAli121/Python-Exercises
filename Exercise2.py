# defining time variable
import time

time = (time.strftime('%H:%M:%S'))   #stores present hour and minute
hour=int(time.strftime('%H'))

hour=input("Enter the hour: ")
print(hour)

if (hour>=4.00 and hour<12.00):
  print("Good Morning Sir!")
elif (hour>=12.00 and hour<17.00):
  print("Good Afternoon Sir!")
elif (hour>=17.00 and hour<21.00):
  print("Good Evening Sir!")
else:
  print("Good Night Sir!")
  