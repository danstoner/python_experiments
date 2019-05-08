import signal
import time

class TimedOutExc(Exception):
    pass

def deadline(timeout, *args):
    def decorate(f):
        def handler(signum, frame):
            raise TimedOutExc()

        def new_f(*args):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)
            return f(*args)
            signal.alarm(0)

        new_f.__name__ = f.__name__
        return new_f
    return decorate

@deadline(5)
def sleep_1():
    print ("Start sleeping 3s...")
    time.sleep(1)
    print ("Done sleeping 3s!")

@deadline(5)
def sleep_10():
    print ("Start sleeping 10s...")
    time.sleep(10)
    print ("Done sleeping 10s!")

def main():
    sleep_1()
    sleep_10()

if __name__ == "__main__":
    main()
