import urllib2 
from multiprocessing.dummy import Pool as ThreadPool 
import time  

time_begin = time.clock()  

urls = [
    'http://zhangguoren.baijia.baidu.com/article/12983'



    # etc.. 
    ]

# Make the Pool of workers
pool = ThreadPool(12) 
# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)
#close the pool and wait for the work to finish 
for row in results:
	print row

pool.close() 
pool.join() 

print "Use time: %s" % (time.clock() - time_begin)