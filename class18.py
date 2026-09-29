#suppose a student 50 m away from the building and
#observe the top at an angle of elevation of 40 degree

# import math
# distance=50
# angle=40
# radian = math.radians(angle)
# height=distance*math.tan(radian)
# print("height of building :",height, "meters")

#      sin
#      |\
# opp  | \ hyp
# tan  |__\ cos
#      adj
#      -dist-


#suppose a drone travells 100 meter at an angle of 30 deg above the horizontal. find its vertical displacement
# import math
# distance=100
# angle=30
# radian=math.radians(angle)
# vertical_distance=distance*math.sin(radian)
# print("vertical distance:", vertical_distance, "meters")

#a drone travells 200 meters at an angle of 60 deg
#find the horizontal distance


# #methods you r aware of different format of date 

# from datetime import datetime
# now = datetime.now()

# print("current date and time :",now)
# print(now.strftime('%d-%m-%Y'))
# print(now.strftime('%d/%m/%Y'))
# print(now.strftime('%B %d,%Y'))

# from datetime import date,datetime
# dob=date(2004,4,14)
# today=date.today()
# age=today.year-dob.year
# if(today.month, today.day)<(dob.month, dob.day):
#     age-=1
# print("age:",age)

# start=date(2026,9,2)
# end=date(2026,9,12)
# difference =end - start
# print("number of days:",difference.days)

#timedalta- deals with entire format of date 
import datetime
from datetime import date,timedelta,datetime
today=date.today()
now=datetime.now()
future_date=today+timedelta(days=7)

print("today:",today)
print("after 7 days:", future_date)
