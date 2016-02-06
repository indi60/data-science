#!/usr/bin/python

import sys, os.path, time


"""======================== Question number 1 ============================"""
"""read a data file"""
def readfile(filename):
	output = []
	rawfile = open(filename+".txt" , 'r')
	#opt 1. avoid . in loop
	for line in rawfile:
		output.append(line.rstrip())
	return output

"""first method to sort the data"""
def sort_method_1(rawdata):
	rawdata.sort()
	return rawdata

"""second method to sort the data"""
#eliminate bucket data
def sort_method_2(filename):
	result = []
	dict = {}
	for i in range(10,100):
		dict[str(i)] = 0
	rawfile = open(filename+".txt" , 'r')
	for item in rawfile:
		dict[item.rstrip()] += 1

	index = 0
	for item in sorted(dict.keys()):
		b = dict[item]
		#xrange() only generate a particular 
		#value at a time and can only be used with the for 
		#loop to print all the values required.
		result[index:index+b] = [item for i in xrange(b)]
		index += b
	return result



"""create an output file"""
def outputFile(filename,input):
	# print input
	out = open("sorted_"+filename+".txt" , 'w')
	for i in input:
		out.write(i + "\n")
	# print "Parsing "+sys.argv[1]+".txt is finish"
	print "Output: sorted_"+filename+".txt"

"""======================================================================="""

def main():
	if len(sys.argv) == 2:
    	#check the file is exist or not
		try: #os.path.exists(sys.argv[1]+".txt"):
			filename = sys.argv[1]
			print "Parsing "+filename+".txt now....."

			start = time.time()
			print "Method 1 is starting now....."
			raw= readfile(filename)
			outputFile(filename,sort_method_1(raw))
			end = time.time()
			time1 = (end-start)
			print 'Time to sort method 1 = ', time1, 's'


			print "--------------------------------"
			print "Method 2 is starting now....."
			start = time.time()
			# raw = readfile(filename)
			outputFile(filename, sort_method_2(filename))
			end = time.time()
			time2 = (end-start)
			print 'Time to sort method 2 = ', time2, 's'

			print "--------------------------------"
			print "Finish..."
			sys.exit(-1)			
		except KeyError:
			print "Cannot find file "+sys.argv[1]+".txt"
		sys.exit(-1)
	else:		
		if len(sys.argv) > 2:
			print "You only allowed to put one parameter" 
		else:
			print "You must put a filename as a parameter!"    	
		sys.exit(-1)


if __name__ == '__main__':
    main()
