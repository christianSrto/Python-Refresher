#Format Specifiers = {value:flags} format a value based on what flags are used

price1 = 3000.14159
price2 = -98700.65
price3 = 1200.34

print(f"Price 1: {price1:.2f}")  # 2 decimal places
print(f"Price 2: {price2:10}")  # Right-aligned in a field of 10 characters
print(f"Price 2: {price2:010}") # Zero-padded in a field of 10 characters
print(f"Price 2: {price2:<10}")  # Left-aligned in a field of 10 characters
print(f"Price 2: {price2:^10}") # Center-aligned in a field of 10 characters
print(f"Price 3: {price3: }")  
print(f"Price 3: {price3:+}") # Space before positive numbers
print(f"Price 3: {price3:-}") # Minus sign before negative numbers
print(f"Price 3: {price3: ,}") # Comma as a thousands separator
print(f"Price 3: {price3: _}") # Underscore as a thousands separator
