import object_storage
import time

creds = open("creds.txt")
account = creds.readline().rstrip()
apikey = creds.readline().rstrip()

sl_storage = object_storage.get_client(account, apikey, datacenter="dal05")
sl_storage["wk7"].create()
sl_storage["wk7"]["file1.txt"].create()
infile = open("fileuploader.py")
start = time.time()
sl_storage["wk7"]["file1.txt"].send(infile)
total = time.time() - start
print sl_storage["wk7"]["file1.txt"].read()
print total
