import time
timestamp = int(time.strftime("%H"))
currenttime = time.strftime('%H:%M:%S')
def greetyouser():
  if timestamp >= 0 and timestamp < 12:
    print("Good Morning Sir")
  elif timestamp >= 12 and timestamp <= 16:
    print("Good Afternoon Sir")
  elif timestamp >= 19:
    print("Good Night Sir")
  else:
    print("Good Evening Sir")
greetyouser()    
print("The current time is", currenttime)
