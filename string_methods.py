name = input("Enter your name: ")
length = len(name)

print(f"Length of your name is: {length}")

#Returns -1 if it doesn;t find the substring
result = name.find("a")
print(f"Index of 'a' in your name is: {result}")
result = name.rfind("a")
print(f"Last index of 'a' in your name is: {result}")

result = name.count("a")
print(f"Count of 'a' in your name is: {result}")

result = name.capitalize()
print(f"Capitalized name: {result}")

result = name.upper()
print(f"Uppercase name: {result}")
result = name.lower()
print(f"Lowercase name: {result}")

#returns True only if the string has numbers exclusively
result = name.isdigit()
print(f"Is name a digit? {result}")

#returns True only if the string has alphabets exclusively
result = name.isalpha()
print(f"Is name an alphabet? {result}")

result = name.replace("a", "o")
print(f"Name after replacing 'a' with 'o': {result}")

#A list of all the methods that can be used on strings
print(help(str))