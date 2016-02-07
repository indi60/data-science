#!/usr/bin/python

import random
from random import randint
import sys, string


"""========================generate the datafile==================="""


def datafile_generator(total_data):
	file = open("age.txt" , 'w')
		
	datarange = range(0, total_data)
	for i in datarange:
		file.write(str(randint(12,80)) + "\n")

	# file = open("blacklist.txt" , 'w')
	# for i in datarange:
	# 	lenghtname = randint(3,9)
	# 	name = randomword(lenghtname)
	# 	phone_number = phone_number_generator(randint(10,12))
	# 	file.write(name + " " +str(phone_number)+ "\n")

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def phone_number_generator(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
"""======================================================================="""




def main():
    if len(sys.argv) == 1:
		limit = 100
   		print "Create " + str(limit)+ " data.."		
		datafile_generator(limit)
    else:
		try:
			limit = int(sys.argv[1])
			print "Creating " + str(limit)+ " data.."
			datafile_generator(limit)
		except ValueError:    		
			print "Parameter should be in Integer, not: \"" + sys.argv[1] + "\" data.."    	
			sys.exit(-1)

if __name__ == '__main__':
    main()
