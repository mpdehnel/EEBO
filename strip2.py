#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import lxml.html
import string
from os import listdir

def strip_file(filename):
	''' Grab all actual raw text that is a somewhere within a <text> tag, from a file within a specified file. '''
	print filename
	string = "".join(lxml.html.document_fromstring(open(filename).read()).xpath("//text//text()")).strip().encode("utf-8")

	# Remove old-worlde 's' and thorns.
	new_string = string.replace("\xc3\x83\xc2\xbe", "th").replace("Å¿", "s").replace("1 line","").lower()
	new_string2 = "".join(c for c in new_string if c not in ('!','?','.',',',':',';','\\','\'','/','(',')','_','&','-'))
	new_string3 = "".join([i for i in new_string2 if not i.isdigit()])
	new_string4 = " ".join(new_string3.split())
	final_string = new_string4

	# print 'Semi-stripped text:\n',string
	# new_string = ''
	# for index in xrange(len(string)):
	# 	# print index
	# 	if ord(string[index]) is 195 and ord(string[index+1]) is 133 and ord(string[index+2]) is 194 and ord(string[index+3]) is 191:
	# 		new_string = new_string+'s'
	# 		# print string[index:index+3]
	# 		index += 3
	# 	new_string += string[index]

	# print ''.join(['s' if (ord(string[index]) is 195 and ord(string[index+1]) is 133 and ord(string[index+2]) is 194 and ord(string[index+3]) is 191) else string[index] for index in xrange(len(string))])
	# 195,133,194,191 are the magic characters that represent the horrible olde-worlde 's', like this 'ſ' or (incorrectly encoded) this 'Å¿' 

	# print ''.join([i if ord(i) < 128 else ''+str(ord(i))+',' for i in new_string])
	return ''.join([i if ord(i) < 128 else '' for i in final_string])


def get_all_text_from_dir(directory):
	files = listdir(directory)
	total_text = []
	for file1 in files:
		# print strip_file(directory+file1)
		total_text.append(strip_file(directory+file1))
	return total_text

print get_all_text_from_dir('../../data/')

# Can join it together to parse if you like
# :-)
# TODO: Spit this data out into raw text format, perhaps with a year attached? Or do we only need to preserve the filename?
