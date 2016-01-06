# EEBO-TCP Hacking

### Martin Dehnel-Wild, Katriel Cohn-Gordon, Reuben Cohn-Gordon.

Basic idea is as follows:

* Take the EEBO text data.
* Strip out the text from the .xml files, giving just a list of words with no punctuation or cruft. (strip2.py)
* For each word: convert it to modern English, using MorphAdorner. (words2.py / words-parallel.py)
* For the modern equivalents, shove it through the etymwn Etymological Dictionary thing to get the closest (non-English) language to which it's related (tsv.py)
* Attach the year of publication of the text to the result
* Produce some nice statistics / visualisations on the percentage of words from different etymological backgrounds over time.
* ???
* Profit

Current state: Parallelised-ish, but seems to spend most of its time in the kernel. Takes a long time, and the parallel version doesn't currently output an answer.

## TODO: 
* Sort the parallelisation, get it spitting out an answer, hopefully speed it up a fair amount too. Try multiprocessing.Pool 
* Links: http://stackoverflow.com/questions/26432411/multiprocessing-dummy-in-python, http://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments/5443941#5443941, http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies, http://www.tutorialspoint.com/python/python_multithreading.htm
* Once this is sorted, push the modern words through the etymological dictionary (tsv.py)

http://morphadorner.northwestern.edu/server/