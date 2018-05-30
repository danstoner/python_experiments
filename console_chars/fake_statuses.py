from __future__ import print_function
import random
from time import sleep
import sys

from terminal import red, green


sym_ok = u'\u2714'  # heavy check mark
sym_err = u'\u2718'  # heavy ballot x (cross mark)
sym_bullet = u'\u2022'  # bullet (dot)


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
        print(green(sym_ok), end="")
    else:
        print(red(sym_err), end="")

