# if __name__ == "__main__": funtions and classes in this module can be reused without 
#                            the main block of code being executed
#                            This script can be imported or run standalone

from script2 import *

def favorite_colour(colour):
    print(f"Your favorite colour is {colour}")


#This only runs if this script is run directly, not if it is imported
def main():
    # Your program goes here
    print("This is script 1")
    favorite_colour("blue")

if __name__ == "__main__":
    main()
   