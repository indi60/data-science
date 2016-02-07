#!/usr/bin/python

import time


def initialize(filename):
	items = set()
	rawfile = open(filename + ".txt" , 'r')
	for line in rawfile:
		items.add(line)
	return items


def check_blacklist(name, phone_number):
	keyword = name+" "+str(phone_number)
	return True if keyword in blacklist else False

def main():
	global blacklist

	# start = time.time()
	blacklist = initialize("blacklist")
	print check_blacklist('agung',6285648077379)
	# end = time.time()
	# time1 = (end-start)
	# print 'Total time search a person and contact: ', time1, 's'


if __name__ == '__main__':
    main()
