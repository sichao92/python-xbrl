#! /usr/bin/env python
# encoding: utf-8
import os
import re
import pandas as pd
from xbrl import XBRLParser, GAAP, GAAPSerializer, DEISerializer

Extracted_fields=['liabilities', 'temporary_equity', 'other_comprehensive_income', 'assets', 'common_shares_issued', 'other_operating_income', 'commitments_and_contingencies', 'income_loss', 'current_assets', 'operating_expenses', 'interest_and_debt_expense', 'common_shares_authorized', 'comprehensive_income_parent', 'net_income_loss', 'common_shares_outstanding', 'net_income_loss_noncontrolling', 'net_cash_flows_investing_discontinued', 'net_cash_flows_discontinued', 'nonoperating_income_loss', 'net_cash_flows_financing_continuing', 'equity_attributable_parent', 'noncurrent_liabilities', 'income_tax_expense_benefit', 'revenue', 'net_cash_flows_investing_continuing', 'cost_of_revenue', 'comprehensive_income', 'net_cash_flows_operating_discontinued', 'stockholders_equity', 'income_from_equity_investments', 'comprehensive_income_interest', 'net_income_shareholders', 'redeemable_noncontrolling_interest', 'net_cash_flows_financing', 'equity_attributable_interest', 'extraordary_items_gain_loss', 'preferred_stock_dividends', 'income_before_equity_investments', 'net_cash_flows_operating', 'equity', 'non_current_assets', 'net_income_parent', 'net_cash_flows_operating_continuing', 'gross_profit', 'costs_and_expenses', 'liabilities_and_equity', 'operating_income_loss', 'net_cash_flows_investing', 'current_liabilities']

xbrl_parser = XBRLParser(precision=0)
# Serialize the GAAP data
serializer = GAAPSerializer()
df = pd.DataFrame(columns=Extracted_fields)
df.index.names = ['Company-date']
xml_path="~/apps/repo/python-xbrl/tests"
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) -1) * '---', os.path.basename(root))
    for file in files:
        print (file)
        if re.match(r"[a-z]{3,5}\-[0-9]{8}\.xml",file):
        #if re.match(r"aaww-20131231.xml",file):
            # Parse an incoming XBRL file
            xbrl = xbrl_parser.parse(file)
            print("Process {}".format(os.path.join(root,file)))
            date_of_doc = re.search(r"[0-9]{8}",file).group()
            # Parse just the GAAP data from the xbrl object
            gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                 	     doc_date=date_of_doc,
                                 	     context="current",
                                 	     ignore_errors=0)
            
            result = serializer.dump(gaap_obj)
            
            #Print out the serialized GAAP data
            print (result)
            attribute = [x.encode('ascii') for x in result[0].keys()]
            values = result[0].values()
            print(values)
            df.loc[file] = values
df.to_csv('./output.csv')
print (df)


## Parse just the DEI data from the xbrl object
#dei_obj = xbrl_parser.parseDEI(xbrl)
#
## Serialize the DEI data
#serializer = DEISerializer()
#result = serializer.dump(dei_obj)
#
## Print out the serialized DEI data
#print (result)
#
#
## Parse just the Custom data from the xbrl object
#custom_obj = xbrl_parser.parseCustom(xbrl)
#
## Print out the Custom data as an array of tuples
#print (custom_obj())
