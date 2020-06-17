# -*- coding:utf-8 -*-
import multiprocessing
import random
import time
from threading import current_thread

from rx import Observable
from rx.concurrency import ThreadPoolScheduler, NewThreadScheduler, CurrentThreadScheduler

start_time = time.time()
def print_obj(obj):
    print obj

def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    # time.sleep(random.randint(5, 20) * .1)
    time.sleep(2)
    return value


# calculate number of CPU's, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count()
pool_scheduler = NewThreadScheduler()

# Create Process 1
# Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
#     .map(lambda s: intense_calculation(s)) \
#     .subscribe_on(pool_scheduler) \
#     .subscribe(on_next=lambda s: print_obj("PROCESS 1: {0} {1}".format(current_thread().name, s)),
#                on_error=lambda e: print_obj(e),
#                on_completed=lambda: print_obj("PROCESS 1 done!"))

# Create Process 2
Observable.range(1, 100) \
    .map(lambda s: intense_calculation(s)) \
    .observe_on(pool_scheduler) \
    .subscribe(on_next=lambda i: print_obj("PROCESS 2: {0} {1}".format(current_thread().name, i)),
               on_error=lambda e: print_obj(e), on_completed=lambda: print_obj("PROCESS 2 done,%s!" %(str(time.time()-start_time))))
#
# Create Process 3, which is infinite
# Observable.interval(1000) \
#     .map(lambda i: i * 100) \
#     .observe_on(pool_scheduler) \
#     .map(lambda s: intense_calculation(s)) \
#     .subscribe(on_next=lambda i: print_obj("PROCESS 3: {0} {1}".format(current_thread().name, i)),
#                on_error=lambda e: print_obj(e))

input("Press any key to exit\n")