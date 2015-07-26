
for i in range(1000):
	for j in range(1000):
		outfile = open("outfile.txt", 'a')
		for k in range(1000):
			outfile.write('a')
		outfile.close()
