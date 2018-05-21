from __future__ import print_function
import random
from time import sleep
import sys

sym_ok = u'\u2714'
sym_err = u'\u2718'


def get_random_status():
    res = random.randint(0, 3)
    sleep(res)
    if res == 0:
        return False
    else:
        return True

print("Begin!")

for x in range (1,25):
    sys.stdout.flush()
    if get_random_status():
        print(sym_ok, end="")
    else:
        print(sym_err, end="")

