import pytz, datetime

year = int(input("Enter year:  "))
month = int(input("Enter month:  "))
date = int(input("Enter date:  "))
hour = int(input("Enter hour:  "))
minute = int(input("Enter minute:  "))

# default time zone is of london 
#converting to date 

user_time = datetime.datetime(year, month, date, hour, minute)

cairo_timezone = pytz.timezone('Africa/Cairo') 
london_timezone = pytz.timezone('UTC')
delhi_timezone = pytz.timezone('Asia/Kolkata')
sydeny_timezone = pytz.timezone('Australia/Sydney')
shanghai_timezone = pytz.timezone('Asia/Shanghai')



cairo_time = pytz.utc.localize(user_time).astimezone(cairo_timezone)
london_time = pytz.utc.localize(user_time).astimezone(london_timezone)
delhi_time = pytz.utc.localize(user_time).astimezone(delhi_timezone)
sydeny_time = pytz.utc.localize(user_time).astimezone(sydeny_timezone)
shanghai_time = pytz.utc.localize(user_time).astimezone(shanghai_timezone)




print("Cairo time is - ", cairo_time.isoformat())
print("london time is - ", london_time.isoformat())
print("Delhi time is - ", delhi_time.isoformat())
print("Syndeny time is - ", sydeny_time.isoformat())
print("Shanghai time is - ", shanghai_time.isoformat())