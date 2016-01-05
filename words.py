#!/usr/bin/env bash

curl --data "spelling=$1&standardize=true&wordClass=&wordClass2=&corpusConfig=eme&media=text&lemmatize=Lemmatize" http://localhost:8182/lemmatizer 2>/dev/null | grep Lemma:

