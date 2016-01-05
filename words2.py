#!/usr/bin/env python
import commands

''' Martin Dehnel-Wild, Katriel Cohn-Gordon 2015-2016 '''

def morph_adorn_word(word):

	''' Make a request to the MorphAdorner Server for the specified word.
		Returns the modern English word.
	'''

	output = commands.getstatusoutput('curl --data "spelling='+word+'&standardize=true&wordClass=&wordClass2=&corpusConfig=eme&media=text&lemmatize=Lemmatize" \
		http://localhost:8182/lemmatizer 2>/dev/null | grep Lemma:')

	return output[1][len('Lemma:\t'):]

# print morph_adorn_word('fantastick')


def load_words_within_file(inputfile1):
	'''	Load a file up, scrape all the words out of it, '''
	words = []
	with open(inputfile1) as inputfile:
		for line in inputfile:
			words.append(line.split())
	return [val for sublist in words for val in sublist]


def search_for_language(word_list):
	''' Get the closest language for each word in the input list. '''
	modern_word_dict = {}
	index = 0
	print 'Total number of words: ', len(word_list)
	for word in word_list:
		try:
			modern_word = morph_adorn_word(word)
			if modern_word in modern_word_dict:
				modern_word_dict[modern_word] += 1
			else:
				modern_word_dict[modern_word] = 1
				# print modern_word, word
		except RuntimeError, e:
			print word,e
		index += 1
		if index%1000 == 0:
			print index
	print 'Total number of words: ', len(word_list)
	return modern_word_dict


print search_for_language(load_words_within_file('test_eebo_output2.txt'))
# search_for_language(load_words_within_file('newfile.txt'))
