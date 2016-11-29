#!/usr/python

try:
	import shodan
except:
	print "[-] Error: You have to install shodan module"
try:
	import argparse
except:
	print "[-] Error: You have to install argparse module"
	exit()
from lib import tools
from lib import shodapi
from pwn import log

def getArgs():
        parser = argparse.ArgumentParser()
        parser.add_argument("--search", help="term to search")
	parser.add_argument("--out-file", help="file to store search result")
	parser.add_argument("--netcams", action="store_true", help="Look for netcams")
	parser.add_argument("--login", action='store_true' ,help="For netcam, try default credentials")
        return parser.parse_args()

if __name__ == "__main__":
	args = getArgs()
	tools.displayIntro()
	tools.displayInit()
	try:
		shod = shodapi.Shodapi()	
	except:
		log.error('nop')

	if args.netcams:
		p = log.progress("Looking for netcams")
		p.status("Crawling IoT...")
		netcams = shod.search("netcam")
		p.success("Got them all !")
		log.info("Found "+str(netcams['total'])+" netcams !")
		for netcam in netcams['matches']:
			log.info(netcam['ip_str']+" located in "+netcam['location']['country_code3'])
		
