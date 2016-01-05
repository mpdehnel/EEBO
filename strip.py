#!/usr/bin/env python2

import sys
import lxml.html

print "".join(lxml.html.document_fromstring(open(sys.argv[1]).read()).xpath(".//body//text()")).strip().encode("utf-8")


