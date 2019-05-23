import time
import sys
import random

from concurrent import futures

TIMEOUT = 5


def task_Sleep(seconds):
    print ("Start sleeping for {0}s...".format(seconds))
    time.sleep(seconds)
    print ("Done sleeping for {0}s!".format(seconds))
    return 1

def main():

    if len(sys.argv) > 1:
        INPUT_TIME = int(sys.argv[1])
        print ("Current script TIMEOUT value is: {0}".format(TIMEOUT))

    else:
        print ("Current script TIMEOUT value is: {0}".format(TIMEOUT))
        print ("Please supply an integer number of seconds to sleep.")
        raise SystemExit


    ex = futures.ProcessPoolExecutor(max_workers=1)
    print('Main thread: starting')
    # map (<task_function_name>, <an iterable that might contain only 1 item>, timeout=<timeout in seconds>)
    results = ex.map(task_Sleep, [INPUT_TIME], timeout=TIMEOUT)
    # must convert to list to trigger TimeoutException
    results_list = list(results)

if __name__ == "__main__":
    main()
