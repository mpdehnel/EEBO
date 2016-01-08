#!/usr/bin/env python
import commands
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
# AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")


''' Martin Dehnel-Wild, Katriel Cohn-Gordon 2015-2016 '''

modern_word_dict = {}
modern_word_list = []


def load_words_within_file(inputfile1):
	'''	Load a file up, scrape all the words out of it, '''
	words = []
	with open(inputfile1) as inputfile:
		for line in inputfile:
			words.append(line.split())
	return [val for sublist in words for val in sublist]

def handle_request(response):
	lemma = 'Lemma:	'
	if response.error:
		print "Error:", response.error
	else:
		temp = response.body[response.body.index(lemma):]
		modern_word = temp[len(lemma):temp.index("\n")]
		# modern_word_list.append(modern_word)
		if modern_word in modern_word_dict:
			modern_word_dict[modern_word] += 1
		else:
			modern_word_dict[modern_word] = 1
		print modern_word, modern_word_dict[modern_word]

def parallel_morph_adorn(inputfile1):
	''' Takes an input file of words. Make a new asynchronous request to the server for each word.
	'''
	word_list = load_words_within_file(inputfile1)
	http_client = AsyncHTTPClient(force_instance=True)
	url="http://localhost:8182/lemmatizer"
	for word in word_list:
		data = "spelling="+word+"&standardize=true&wordClass=&wordClass2=&corpusConfig=eme&media=text&lemmatize=Lemmatize"
		req = HTTPRequest(url, method="POST", body=data)
		http_client.fetch(req,handle_request)

parallel_morph_adorn('test_eebo_output2.txt')
# parallel_morph_adorn('small.txt')
print 'Starting Lemmatization'
loop = IOLoop.instance()
if __name__ == "__main__":
    loop.start()

# print modern_word_list

# This seems to work pretty well. Now just need to work out how to get the output once it's done (rather than sitting in the loop forever).
# Perhaps pickle it every 10,000 entries?