import time
import threading
import multiprocessing


def yes(no) :
    while True:
        print"yes - %d\n" % no
        time.sleep(0.5)

def no(no) :
    while True:
        print"no - %d\n" % no
        time.sleep(0.5)

# t1 = threading.Thread(target=yes, args=(1,))
# t2 = threading.Thread(target=yes, args=(2,))

# t1.start()
# t2.start()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=yes, args=(1,))
    p2 = multiprocessing.Process(target=yes, args=(2,))
    p1.start()
    p2.start()