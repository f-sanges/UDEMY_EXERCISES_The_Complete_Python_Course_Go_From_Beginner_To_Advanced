import time

print("The time is: ", time.time())

print("The time human readable is: ", time.ctime())

later = time.time() + 15

print('15 seconds from now: ', time.ctime(later))

# show stats of a file
import os, sys

stinfo = os.stat('D:\prova_python.txt')
print(stinfo)


print('Access time of prova_python: %s' % stinfo.st_atime)
print('Modified time of prova_python is: %s' % stinfo.st_mtime)


print('gmtime : ', time.gmtime())
print('localtime : ', time.localtime())


