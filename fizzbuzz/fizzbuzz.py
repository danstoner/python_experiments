from __future__ import print_function

i = 1
while i <= 100:
    if i % 3 == 0:
        print ("Fizz", end = "")
    if i % 5 == 0:
        print ("Buzz", end = "")
    if not ((i % 3 == 0) or (i % 5 == 0)):
        print (i, end = "")

    print ("")
    i += 1
