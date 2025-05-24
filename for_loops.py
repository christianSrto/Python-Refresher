#For Loops = execute a block of code a fixed number of times

for counter in range(1, 11):
    print(counter)

for counter in reversed(range(1,11, 2)):
    print(counter)

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in range(1,21):
    #skips the number 13 by using continue
    if x == 13: 
        continue
    else:
        print(x)

for x in range(1,21):
    #stops at 13
    if x == 13: 
        break
    else:
        print(x)


#Nested Loops = A loop within another loop 

for x in range(3):
    for y in range (0,10):
        print(y, end="")
    print()