from __future__ import print_function

i = 1
while i <= 15:
    if not i % 3 :
        print ("Fizz", end = "")
    if not i % 5 :
        print ("Buzz", end = "")
    if not (not (i % 3) or not (i % 5)):
        print (i, end = "")

    print ("")
    i += 1
