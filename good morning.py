import time
timestamp = int(time.strftime("%H"))
currenttime = time.strftime('%H:%M:%S')
def greetuser():
  if timestamp >= 0 and timestamp < 12:
    print("Good Morning Sir")
  elif timestamp >= 12 and timestamp <= 16:
    print("Good Afternoon Sir")
  elif timestamp >= 19:
    print("Good Night Sir")
  else:
    print("Good Evening Sir")
greetuser()    
print("The current time is", currenttime)
