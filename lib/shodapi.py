#!/usr/python

import tools
import shodan
from pwn import log

class Shodapi:

	def __init__(self):
		api_key = tools.getAPIKey()
		self.api = shodan.Shodan(api_key)	
		
	def search(self, terms):
		results = self.api.search(terms)
		return results

	def netcams(self):
		p = log.progress("Looking for netcams")
                p.status("Crawling IoT...")
                netcams = self.search("netcam")
                p.success("Got them all !")
                log.info("Found "+str(netcams['total'])+" netcams !")
                for netcam in netcams['matches']:
                        log.info(netcam['ip_str']+" located in "+netcam['location']['country_code3'])

