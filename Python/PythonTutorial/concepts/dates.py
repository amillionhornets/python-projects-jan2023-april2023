import datetime

# Get current date 
today = current_date = datetime.date.today()
print(today)
# Create date (Year, day, month)
date1 = datetime.date(2004, 9, 11)
print(date1)

print("Year: ", today.year)
print("Year: ", today.month)
print("Year: ", today.day)

# Create time(hours, mins, secs, ms)
time1 = datetime.time(10, 45, 30, 45667)
print(time1)

# date time obj (Year, day, month, Hour, mins, secs, microseconds)
datetimeObj = datetime.datetime(2004, 9, 11, 10, 45, 30, 45667)
print(datetimeObj)
print(datetimeObj.date())
print(datetimeObj.time())
# Gets current datetime
currentDateTime = datetime.datetime.now()
print(currentDateTime)
# The difference between two date times is timedelta
currentTime = datetime.datetime.now()
nextYear = datetime.datetime(2024, 1, 1, 0, 0, 0, 0)
timeRemaining = nextYear - currentTime

print(timeRemaining)

# strftime date time to str A = weekday name, B = Month, d = day, Y = year
stringDate = currentTime.strftime("%A, %B %d, %Y")
print(stringDate)

# strptime str to date
dateString = "21 June, 2023"
dateObj = datetime.datetime.strptime(dateString, "%d %B, %Y")
print(dateObj)