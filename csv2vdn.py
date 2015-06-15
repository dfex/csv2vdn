#!/usr/bin/env python

## csv2vdn.py - 15/06/2015
## ben.dale@gmail.com
## Convert CSV indials to Freeswitch XML

import sys
import csv
from lxml import etree
from pprint import pprint

sys.stdout.write("csv2vdn\n\n")
if len(sys.argv) != 2:
	sys.stdout.write("Error: Missing parameter\n")
	sys.stdout.write("Usage: csv2vdn <indial-list.csv>\n")
	sys.exit()


sys.stdout.write('Opening ' + sys.argv[1] + '\n')
sys.stdout.flush()

try:
	indialfile = open(str(sys.argv[1]),'r')
except:
	sys.stdout.write('File processing error - does ' + sys.argv[1] + ' exist?\n')
	sys.stdout.flush()
else:
	indialdict = csv.DictReader(indialfile)
	sys.stdout.write('Processing: ')
	for row in indialdict:
		outfd = open(row['VDN']+"_inbound.xml",'a')
		extension = etree.Element("extension", name=row['Indial'])
		condition = etree.SubElement(extension, "condition", field="destination_number", expression=row['Indial'])
		action = etree.SubElement(condition, "action", application="bridge", data="sofia/internal/" + row['VDN'] + "@192.168.2.37:5060")
		outfd.write(etree.tostring(extension, pretty_print="True"))
		outfd.close()
		sys.stdout.write('.')
		sys.stdout.flush()
	sys.stdout.write('\nClosing ' + sys.argv[1] + '\n')
	sys.stdout.flush()
	indialfile.close()

		

