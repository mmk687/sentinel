#!/usr/python

import argparse

#args
def getArgs():
        parser = argparse.ArgumentParser()
        parser.add_argument("--search", help="term to search")
        parser.add_argument("--file", help="file to store search result")
        parser.add_argument("--netcams", action="store_true", help="Look for netcams")
#        parser.add_argument("--login", action='store_true' ,help="For netcam, try default credentials")
        return parser.parse_args()

#API
def getAPIKey():
	with open('key', 'r') as f:
		return f.read().strip()
		f.close()

#display tools

def displayIntro():
        logInfo("Please use this for legal purposes")

def displayInit():
	logInfo("Initializing shodan API")

def logInfo(msg):
        print "[\033[92m*\033[0m]"+ msg

def logError(msg):
        print "[\033[31m-\033[0m]"+msg

