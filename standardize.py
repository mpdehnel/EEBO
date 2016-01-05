#!/usr/bin/env python2

import sys, requests, json

word = sys.argv[1]
params = {"spelling": word, "corpusConfig": "eme", "media": "json", "standardize": "Standardize"}

result = requests.get("http://localhost:8182/spellingstandardizer", params=params).content
print json.loads(result)["SpellingStandardizerResult"]["standardSpelling"]
