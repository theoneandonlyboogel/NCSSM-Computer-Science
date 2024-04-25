import threading
import time
from countdown import countdown



if __name__ == "__main__":

    x = threading.Thread(target=countdown(mins=0, secs=10))
    x.start()

    # Run some other code in parallel with the timer

    x.join() # will wait for the timer function to finish
    print('All done')
