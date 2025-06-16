# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from API's 
#                  threading.Thread(target=my_function)

import threading 
import time

def walk_dog(name):
    time.sleep(8)
    print(f"you finish walking {name}")

def take_out_trash():
    time.sleep(3)
    print("You take out the trash")

def get_mail():
    time.sleep(5)
    print("You get the mail")

print("chores without multithreading:")
walk_dog("Scooby")
take_out_trash()
get_mail()


print("\nchores with multithreading:")
#args is a tuple; always end with , if function only takes 1 argument
thread1 = threading.Thread(target=walk_dog, args=("Scooby",))
thread1.start()

thread2 = threading.Thread(target=take_out_trash)
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()

#waits for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All chores are done")