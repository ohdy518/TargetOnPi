import time
print("Target on pi")
input("Press <Enter> to start: ")
_1 = round(time.time(), 2)
input("Press <Enter> to stop: ")
_2 = round(time.time(), 2)
sub = round(_2 - _1, 2)
is_pi = None
pi = 3.14
timechange = 0
if sub == pi:
    is_pi = True
else:
    is_pi = False

timechange = sub - pi
print(f"Start time: {_1}")
print(f"End time: {_2}")
print(f"Elapsed time: {sub}")
print(f"Pi: {pi}")
print(f"Is pi: {is_pi}")
print(f"Time gap: {timechange}")