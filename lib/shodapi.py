#!/usr/python

import tools
import shodan
from pwn import log

class Shodapi:

	def __init__(self):
		api_key = tools.getAPIKey()
		self.api = shodan.Shodan(api_key)	
		self.results = ""
	def resetResults(self):
		self.results = ""
		
	def setResults(self, res):
		self.results = res

	def customSearch(self, terms):
		self.resetResults()
		result = self.api.search(terms)
	        self.setResults(result)
		p = log.progress("Looking for '"+terms+"' into the deep IoT kingdom")
                p.status("Digging...")
                p.success("Got them all !")
                log.info("Found "+str(result['total'])+" "+terms+" things !")
                for thing in result['matches']:
                        log.info(thing['ip_str']+" located in "+unicode(thing['location']['country_name']))
		
	def netcams(self):
		p = log.progress("Looking for netcams")
                p.status("Crawling IoT...")
                netcams = self.api.search("netcam")
		self.setResults(netcams)
                p.success("Got them all !")
                log.info("Found "+str(netcams['total'])+" netcams !")
                for netcam in netcams['matches']:
                        log.info(netcam['ip_str']+" located in "+netcam['location']['country_code3'])
	
	def writeToFile(self, filename):
		lf = "\n"
		p = log.progress("Writing results into "+filename+"...")
		p.status("Writing...")
		with open(filename, 'w') as f:
			for line in self.results['matches']:
				f.write(line['ip_str']+" located in "+unicode(line['location']['country_name'])+lf)
			f.close()
		p.success("Done !")
