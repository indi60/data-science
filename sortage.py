#!/usr/bin/python

import sys, os.path, time


"""This is the main parse, this method will read
the inputfile and classify the number inside dictionary"""
def readAndSort(filename):
	result = []
	dict = {}
	for i in range(0,100):
		dict[str(i)] = 0
	rawfile = open(filename+".txt" , 'r')
	for item in rawfile:
		dict[item.rstrip()] += 1

	index = 0
	for item in sorted(dict.keys()):
		b = dict[item]
		result[index:index+b] = [item for i in xrange(b)]
		index += b
	return result

"""This method will create an output file"""
def outputFile(filename,input):
	out = open("sorted_"+filename+".txt" , 'w')
	for i in input:
		out.write(i + "\n")
	print "Output: sorted_"+filename+".txt"

"""This is a main method"""
def main():
	if len(sys.argv) == 2:
		try:
			filename = sys.argv[1]
			print "Parsing "+filename+".txt now....."
			# start = time.time()
			outputFile(filename, readAndSort(filename))
			# end = time.time()
			# time2 = (end-start)
			# print 'Time to sort method 1 = ', time1, 's'
			print "Finish..."
		except KeyError:
			print "Cannot find file "+sys.argv[1]+".txt"
		sys.exit(-1)
	else:		
		if len(sys.argv) > 2:
			print "You're only allowed to sort one file" 
		else:
			print "You must put a filename as a parameter!"    	
		sys.exit(-1)

if __name__ == '__main__':
    main()
