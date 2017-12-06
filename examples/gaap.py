#! /usr/bin/env python
# encoding: utf-8
import pandas as pd
from xbrl import XBRLParser, GAAP, GAAPSerializer, DEISerializer
  
xbrl_parser = XBRLParser(precision=0)

# Parse an incoming XBRL file
xbrl = xbrl_parser.parse(open("../tests/aaww-20131231.xml"))

# Parse just the GAAP data from the xbrl object
gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                 doc_date="20131231",
                                 context="current",
                                 ignore_errors=0)

# Serialize the GAAP data
serializer = GAAPSerializer()
result = serializer.dump(gaap_obj)

attribute = [x.encode('ascii') for x in result[0].keys()]
values = result[0].values()
df = pd.DataFrame(columns=attribute,index=['aaww'])
df.loc['aaww'] = values
print (df)


## Parse just the DEI data from the xbrl object
#dei_obj = xbrl_parser.parseDEI(xbrl)
#
## Serialize the DEI data
#serializer = DEISerializer()
#result = serializer.dump(dei_obj)
#
## Print out the serialized DEI data
#print (result[0])
#
#
## Parse just the Custom data from the xbrl object
#custom_obj = xbrl_parser.parseCustom(xbrl)
#
## Print out the Custom data as an array of tuples
#print (custom_obj())
