import math
i = int(1)
pi = int(0)
times = int(input("Enter a positive integer as precision"))
for i in range(0,times):
    pi = pi + 1 / i**2
    i = i + 1
pi = pi * 6
pi = math.sqrt(pi)
print(pi)
