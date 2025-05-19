import math
x = 3.14
y= 2
z= 1
i = -2

y -= 1
print(y)
z += 1
print(z)
x *= y
print(x)
x /= z
print(x)
z **= 2
print(z)
y %= 2
print(y)

result = round(x)
print(result)

result = abs(i)
print(result)

#pow(base, exponent)
result = pow(x, y)
print(result)

#divmod(dividend, divisor)
result = divmod(x, y)
print(result)


result = max(x, y)
print(result)

result = min(x, y)
print(result)

result = sum([x, y, z])
print(result)

result = sorted([x, y, z])
print(result)

result = all([x, y, z])
print(result)   

result = any([x, y, z])
print(result)

result = bin(y)
print(result)

result = oct(y)
print(result)

result = hex(y)
print(result)

result = complex(x)
print(result)

math = math.sqrt(x)
print(math)

result = math.ceil(x)
print(result)
result = math.floor(x)
print(result)



print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
