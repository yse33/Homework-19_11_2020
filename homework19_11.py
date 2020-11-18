#exercise 1
vowels = "AaEeIiOoUu"
str = str(input())
a = 0
for i in str:
    if i in vowels:
        while a < 4:
            print(i, end="")
            a += 1
    else:
        print(i, end="")
    a = 0

#exercise 2
print()
num = int(input())
len = 1
true = 1
while true == 1:
    if num / 10 > 1:
        len = len + 1
        num = num / 10
    else:
        true = 0
print(len)

#exercise 3
import math
number = float(input())
count = 0
while number > 2:
    number = math.sqrt(number)
    count = count + 1
print(count)

#exercise 4
n = int(input())
prime = 1
all = 0
for i in range(2,n+1):
    prime = 1
    for y in range(2,i):
        if (i % y) == 0:
            prime = 0
            break
    if prime == 1:
        all = all + i
print(all)             