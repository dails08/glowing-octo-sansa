import urllib2


for i in range(arg[1], arg[2]):
    print "downloading "+str(i)+"..."
    url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-2gram-20090715-" + str(i) + ".csv.zip"
    f = urllib2.urlopen(url)
    with open("/gpfs/gpfsfpo/"+str(i) + ".zip", "wb") as filename:
        filename.write(f.read())


