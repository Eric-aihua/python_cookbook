# -*- coding:utf-8 -*-
# @Author：sunaihua 
import ray
import time

ray.init()


@ray.remote
def cost(x):
    time.sleep(2)
    return x * x


s = time.time()
futures = [cost.remote(x) for x in range(10)]
print(ray.get(futures), "spend %s s" % str(time.time() - s))
