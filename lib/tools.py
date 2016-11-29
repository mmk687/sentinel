#!/usr/python

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

