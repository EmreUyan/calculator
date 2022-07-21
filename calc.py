import math
from math import sqrt

print(">>>")

s1 = int(input("1st Number: "))
s2 = int(input("2nd Number: "))
s3 = input("Operator: ")

if s3 == "+" :
    print(">>>")
    print(s1 + s2)

elif s3 == "-" :
    print(">>>")
    print(s1 - s2)

elif s3 == "*" :
    print(">>>")
    print(s1 * s2)

elif s3 == "/" :
    print(">>>")
    print(s1 / s2)

elif s3 == "k" :
    print(">>>")
    print(s1 * s1 + s2 * s2)

elif s3 == "kk" :
    print(">>>")
    print(sqrt(s1))

else:
    print(">>>")
    print("Error. (Please type an operator)")

    
