import time 


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    sec = x % 60 
    mins = int(x / 60) % 60
    hrs = int(x/3600)
    print(f"{hrs:02}:{mins:02}:{sec:02}")
    time.sleep(1)

print("Times Up!")