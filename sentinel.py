#!/usr/python
#-*- coding: utf-8 -*-

try:
	import shodan
except:
	print "[-] Error: You have to install shodan module"
	exit()
try:
	import argparse
except:
	print "[-] Error: You have to install argparse module"
	exit()

from lib import tools
from lib import shodapi
from pwn import log

if __name__ == "__main__":
	args = tools.getArgs()
	tools.displayIntro()
	tools.displayInit()
	try:
		shod = shodapi.Shodapi()	
	except:
		log.error('Error: check your key, or internet connection')
	if args.netcams:
		shod.netcams()
	elif args.search:
		shod.customSearch(args.search)

	if args.file:
		shod.writeToFile(args.file)
	
	log.warning("Please secure your IoT devices ...")
