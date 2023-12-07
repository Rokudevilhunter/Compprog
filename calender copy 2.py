import datetime
import calendar

def findDay(date):
	born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
	return (calendar.day_name[born])

print("The date must be in 'MM DD YYYY' format")
date = input("The date:  ")


# while date not in '%m %d %Y':
# 	print("The date must be in 'MM DD YYYY' format")
# 	date = input("The date:  ")
# 	if date in '%m %d %Y':
# 		print(findDay(date))
# else:
# 	print(findDay(date))

while 0 == 0:
	if date in '%m %d %Y':
		print(findDay(date))
	else:
		print(findDay(date))
		print("The date must be in 'MM DD YYYY' format")
		date = input("The date:  ")


