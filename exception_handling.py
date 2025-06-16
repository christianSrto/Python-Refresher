# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally


try:
    number = int(input("Enter a number: "))
    print (1/number)
except ZeroDivisionError:
    print("you can't divide by 0")
except ValueError:
    print("Enter a valid integer")

# this is bad practice as it catches all errors
except Exception:
    print("I don't know what caused this error")
    
#always executes
finally:
    print("Do some cleanup here")