#!/usr/bin/python

from random import randint
import sys, os, re, operator
import time

"""create a data file"""
def dafafile_Maker():
	file = open("age.txt" , 'w')
 
	for i in range(1, 1000000):
		file.write(str(randint(12,60)) + "\n")

	file = open("blacklist.txt" , 'w')
	for i in range(1, 1000000):
		file.write(str(randint(12,60)) + "\n")


"""create read the file"""
def readfile():
	output = []
	rawfile = open("age.txt" , 'r')
	for line in rawfile:
		output.append(line.rstrip())
	return output

"""sort a data file"""
def sort(rawdata):
	rawdata.sort()
	return rawdata

"""create an output file"""
def outputFile(input):
	# print input
	out = open("sorted_age.txt" , 'w')
	for i in input:
		out.write(i + "\n")
	



def main():
	dafafile_Maker()

	start = time.time()
	raw = readfile()
	outputFile(sort(raw))
	end = time.time()

	time1 = (end-start)
	print 'Time to sort = ', time1*1000, 'ms'


if __name__ == '__main__':
    main()
