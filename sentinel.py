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
		log.error('nop')
	if args.netcams:
		shod.netcams()
	elif args.search:
		p = log.progress("Looking for '"+args.search+"' into the deep IoT kingdom")
		p.status("Digging...")
		result = shod.search(args.search)
		p.success("Got them all !")
		log.info("Found "+str(result['total'])+" "+args.search+" things !")
		for thing in result['matches']:
			log.info(thing['ip_str']+" located in "+unicode(thing['location']['country_name']))
