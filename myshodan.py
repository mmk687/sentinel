#!/usr/python

import shodan
import sys
try:
	import argparse
except:
	print "You have to install argparse module"
	exit()
from lib import tools


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
