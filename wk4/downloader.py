import urllib2
import sys


for i in range(int(sys.argv[1]), int(sys.argv[2])):
    print "downloading "+str(i)+"..."
    url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-2gram-20090715-" + str(i) + ".csv.zip"
    f = urllib2.urlopen(url)
    with open("/data/wk4lab/"+str(i) + ".zip", "wb") as filename:
        filename.write(f.read())
