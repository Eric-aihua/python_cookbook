# encoding:utf-8

"""
contenxt的内容会被保存在checkpointPath中，重启时，会从该位置的文件钟加载context
"""
from __future__ import print_function

import os
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def createContext(host, port, outputPath):
    # If you do not see this printed, that means the StreamingContext has been loaded
    # from the new checkpoint
    print("Creating new context")
    if os.path.exists(outputPath):
        os.remove(outputPath)
    sc = SparkContext(appName="PythonStreamingRecoverableNetworkWordCount")
    ssc = StreamingContext(sc, 1)

    # Create a socket stream on target ip:port and count the
    # words in input stream of \n delimited text (eg. generated by 'nc')
    lines = ssc.socketTextStream(host, port)
    words = lines.flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

    def echo(time, rdd):
        counts = "Counts at time %s %s" % (time, rdd.collect())
        print(counts)
        print("Appending to " + os.path.abspath(outputPath))
        with open(outputPath, 'a') as f:
            f.write(counts + "\n")

    wordCounts.foreachRDD(echo)
    return ssc

if __name__ == "__main__":
    # If the checkpointDirectory exists, then the context will be recreated from the checkpoint data. If the directory does not exist (i.e., running for the first time),
    # then the function functionToCreateContext will be called to create a new context and set up the DStreams
    ssc = StreamingContext.getOrCreate('/tmp/spark/recovery',
                                       lambda: createContext('10.5.24.137', 9999, './recover output'))
    ssc.start()
    ssc.awaitTermination()