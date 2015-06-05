import urllib2
import sys


for i in range(sys.args[1], sys.args[2]):
    print "downloading "+str(i)+"..."
    url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-2gram-20090715-" + str(i) + ".csv.zip"
    f = urllib2.urlopen(url)
    with open("/gpfs/gpfsfpo/"+str(i) + ".zip", "wb") as filename:
        filename.write(f.read())


