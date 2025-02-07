"""
Start
print "a. Count in 10s from 0 to 100:"
for i from 0 to 100 step 10
    print i
print

print "b. Count down from 20 to 1:"
for i from 20 to 1 step -1
    print i
print

print "c. Print n stars:"
get num_stars
for _ from 1 to num_stars
    print "*"
print

print "d. Print n lines of increasing stars:"
get num_lines
for i from 1 to num_lines
    print "*" * i
End
"""
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print("\nb. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print("\nc. Print n stars:")
num_stars = int(input("Number of stars: "))
for _ in range(num_stars):
    print("*", end='')
print()

print("\nd. Print n lines of increasing stars:")
num_lines = int(input("Number of lines: "))
for i in range(1, num_lines + 1):
    print("*" * i)