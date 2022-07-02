import time

time_start=time.time()
time_end=time.time()
print("Time start is :"+ str(time_start))
print("Time end is :"+ str(time_end))
print(time_end-time_start)
if time_end-time_start>30:
    print("oh")