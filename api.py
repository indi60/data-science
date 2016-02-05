#!/usr/bin/python

import time


def initialize(filename):
	items = set()
	rawfile = open(filename + ".txt" , 'r')
	for line in rawfile:
		items.add(line)
	return items


def check_blacklist(name, phone_number):
	find = name+" "+str(phone_number)
	return True if find in blacklist else False

def main():
	global blacklist

	print "-----------------------------------"
	start = time.time()
	blacklist = initialize("blacklist")
	print check_blacklist('oeaqnll',51963794481)
	end = time.time()

	time1 = (end-start)
	print 'Time to sort method 1 = ', time1, 's'
	print "-----------------------------------"


if __name__ == '__main__':
    main()
