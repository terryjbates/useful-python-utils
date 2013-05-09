#!/usr/bin/env python
'''
Script to illustrate to my forgetfulness on how to use myThread.py
'''

def generate_something:
.....

hosts = ['foo', 'bar', 'baz']

def main():
    # Create a list of functions you want to use from those already defined
    funcs = [generate_andrew_stats]
    # Get number of hosts and number of functions
    nhosts = range(len(hosts))
    nfuncs = range(len(funcs))

    print '\n*** Generating threads ***'

    # Create an empty list for threads
    threads = []

    # Remember that we create a range based on the len of the number of hosts.
    # [0,1,2, etc...]
    for i in nhosts:
        print "creating new thread for", hosts[i]
        t = MyThread(funcs[0], (hosts[i],),
                hosts[i])
        # Append to our list of threads
        threads.append(t)

    # Begin our run. Starting up all our threads via a loop.
    for i in nhosts:
        print 'starting', funcs[0].__name__, 'for', hosts[i]
        threads[i].start()

    # Use the .join operator to synchronize execution of the threads.
    # This blocks calling thread until the thread whose join() method is called is terminated.
    # Since this script is calling .join() on *all* the threads, it will not end until all
    # threads are ended. 
    for i in nhosts:
        threads[i].join()
        print threads[i].getResult()
        print 'name ', funcs[i].__name__

    print 'all DONE.'


if __name__ == '__main__':
    main()
