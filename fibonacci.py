import sys
import cs50

a=0
a=int(a)
b=sys.argv[1]
b=int(b)
c=0
n_line=sys.argv[2]
n_line=int(n_line)
print("The Fibonacci serie is the following: ")

for i in range(n_line):
    print("{:>8}".format(a), end= " ")
    print("{:>8}".format(b), end= " ")
    c=a+b
    a,b=b,c
    print("{:>8}".format(c))