from datetime import datetime

# Create a datetime object representing the current date and time
now = datetime.now()

# Access various attributes of the datetime object
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

# Format the datetime object as a string
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the results
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)
print("Microsecond:", microsecond)
print("Formatted Datetime:", formatted_datetime)
