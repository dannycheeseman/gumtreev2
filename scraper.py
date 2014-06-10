import scraperwiki

# Blank Python

 import urllib2, time, sys

#int(sys.argv[1])

#for i in range(8, 18): # The two numbers indicates the first and the last patent website that will be downloaded
for i in range(int(sys.argv[1]), int(sys.argv[2])):
   page = urllib2.urlopen("http://capetown-westerncape.gumtree.co.za/f-Jobs-W0QQAdTypeZ1QQCatIdZ%d" % (i))
   f = open("Files/patent_%d.htm" % i, 'w')
   f.write(page.read())
   f.close
   time.sleep(5) # How many seconds the script waits before downloading the next page