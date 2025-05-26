# Default Arguments = a default value for a parameter
#                     defaut is used when that argument is not passed
import time

def net_price(list_price, discount =0, tax = 0.13):
    return list_price*(1 - discount) * (1 + tax)


print(net_price(100))  # Uses default discount and tax 

def count(end, start=0): #default arguments should be last
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)  

count(5) 