#!/usr/bin/env python2

import sys, requests, json

word = sys.argv[1]
params = {"spelling": word, "corpusConfig": "eme", "media": "json", "standardize": "true", "lemmatize": "Lemmatize"}

result = requests.get("http://localhost:8182/lemmatizer", params=params).content
print json.loads(result)["LemmatizerResult"]["lemma"]
