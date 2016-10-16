#!/usr/bin/python

# output
print 'hello, world'
print 'hello,', 'world'
print '1 + 2 =', 1 + 2

# input
name = raw_input("Please input your name: ")
print 'hello, ', name

# if/else
age = 3
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >= 6:
    print 'your age is', age
    print 'teenage'
else:
    print 'your age is', age
    print 'kid'

x = 1
if x:
    print 'True'

# for
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in range(101):
    sum = sum + x
print sum

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# function
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

my_abs(100)

def nop():
    pass
