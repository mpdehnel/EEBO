#!/usr/bin/env python
from itertools import repeat
import csv
import pickle

def read_tsv(filename):
	output = []
	with open(filename,'rb') as tsvin:
	    tsvin = csv.reader(tsvin, delimiter='\t')

	    for row in tsvin:
	        # if row[0][:3] == 'eng' and row[1][:10] == 'rel:etymol':
	        if row[1][:10] == 'rel:etymol':
				output.append((row[0][5:],(row[2][:3],row[2][5:])))
	return output

# et_dict = dict(read_tsv('/home/martin/etymwn/etymwn.tsv'))
et_dict = dict(read_tsv('../etymwn/etymwn.tsv'))
# file1 = open('et_dict2.dict', "w")
# pickle.dump(et_dict,open( "/home/martin/etymwn/et_dict2.dict","wb"))
# file1.close()

def search_root(word,last):
	''' 
		Search for the closest non-English language of origin of the word.
		If it returns 'eng' or 'enm' as the closest 'non-English' language of origin,
		 the dictionary file given to it got into an infinite loop, e.g. 'hello -> hello'
	'''
	
	root = et_dict[word[1]] # This looks like ('lat', 'abnegation')
	''' If the recursion gets into a loop, i.e. this layer's 'answer' is the same as 
	     the layer that called it, stop it to prevent an infinite loop. '''
	if root[0] in ['eng','enm']:
		if root is last:
			return last
		else:
			return search_root((root[0],root[1],word[1]),root)
	else:
		return (root[0],root[1],word[1])


def search_word(word):
	try:
		output = search_root(('eng',word,word),None)
		return output[0],word
	except KeyError, e:
		print 'Word \'' + word + '\' not found. Skipping.'
		return word
	
def load_words_within_file(inputfile1):
	'''	Load a file up, scrape all the words out of it, '''
	words = []
	with open(inputfile1) as inputfile:
		for line in inputfile:
			words.append(line.split())
	return [val for sublist in words for val in sublist]

def search_for_language(word_list):
	''' Get the closest language for each word in the input list. '''
	for word in word_list:
		try:
			print search_word(word)
		except RuntimeError, e:
			print word,e # This should never get called. If it does, something's gone seriously wrong!
	return


# print search_word('abnegation')
# print search_word('flute')
# print search_word('delight')

search_for_language(load_words_within_file('newfile.txt'))
