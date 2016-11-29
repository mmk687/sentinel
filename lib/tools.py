#!/usr/python

def displayIntro():
	print "[+] Please use this for legal purposes"

def getAPIKey():
	with open('../key', 'r') as f:
		print f.read()
		f.close()
