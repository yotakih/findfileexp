#!/usr/bin/python3
#-*-coding: utf-8-*-
import glob
import getopt
import sys

def findfileexp(finddir,exp):
	for f in glob.iglob('**/' + exp,recursive=True):
		yield f

def ana_opt(argv):
	opts,args = getopt.getopt(argv,'d:e:')
	d = ''
	e = ''
	for k,v in opts:
		if k == '-d':
			d = v
		elif k == '-e':
			e = v
	if d == '' or e == '':
		raise ValueError('args error')
	return d,e

if __name__ == '__main__':
	try:
		dir,exp = ana_opt(sys.argv[1:])
		for fl in findfileexp(dir,exp):
			print(fl)
	except ValueError as e:
		print(e)
