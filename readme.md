= EEBO-TCP Hacking =

Martin Dehnel-Wild, Katriel Cohn-Gordon, Reuben Cohn-Gordon.

Basic idea is as follows:

 *Take the EEBO text data.
 *Strip out the text from the .xml files, giving just a list of words with no punctuation or cruft. (strip2.py)
 *For each word: convert it to modern English, using MorphAdorner
 *For the modern equivalents, shove it through the etymwn Etymological Dictionary thing to get the closest (non-English) language to which it's related
 *Attach the year of publication of the text to the result
 *Produce some nice statistics / visualisations on the percentage of words from different etymological backgrounds over time.
 *???
 *Profit