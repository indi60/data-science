#!/usr/bin/python

import time

def initialize(filename):
	output = {}
	rawfile = open(filename + ".txt" , 'r')
	for line in rawfile:
		data = line.rstrip().split(" ")
		key= data[0] + "-"+data[1]
		output[key] = [data[0], data[1]]		
	return output	


def check_blacklist(name, phone_number):
	key = name+"-"+str(phone_number)
	return True if key in blacklist.keys() else False


def main():
	start = time.time()
	global blacklist
	blacklist = initialize("blacklist")
	print check_blacklist('oeaqnll',51963794481)
	end = time.time()

	time1 = (end-start)
	print 'Time to sort method 1 = ', time1, 's'


if __name__ == '__main__':
    main()
