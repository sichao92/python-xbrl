#! /usr/bin/env python
# encoding: utf-8

from xbrl import XBRLParser
from xbrl import GAAP
from xbrl import GAAPSerializer
from xbrl import DEISerializer
from xbrl import XBRLParserException
import pytest
import sys
import os
import six

try:
    import __pypy__
except ImportError:
    __pypy__ = None

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

sys.path.insert(0, os.path.abspath('python-xbrl'))


def test_parse_empty_file():
    xbrl_parser = XBRLParser()
    file_to_parse = "nothing.xml"
    with pytest.raises(XBRLParserException):
        xbrl_parser.parse(file_to_parse)


def test_open_file_handle():
    xbrl_parser = XBRLParser()
    file_to_parse = "sam-20130629.xml"
    try:
        xbrl_parser.parse(file(file_to_parse))
    except NameError:
        pass


def test_parse_GAAP10Q_RRDonnelley():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "sam-20130629.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 98032.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 12107.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 5417.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == 19715.0
    assert result.data['liabilities_and_equity'] == 60263.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 65084.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 253536.0
    assert result.data['net_income_loss'] == 19715.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 19715.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 19715.0
    assert result.data['income_before_equity_investments'] == 31822.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 376766.0
    assert result.data['gross_profit'] == 97132.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 138996.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0


def test_parse_GAAP10K_RRDonnelley():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "sam-20131228.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 104377.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 0.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 9556.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == 29120.0
    assert result.data['liabilities_and_equity'] == 69900.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 0.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 302085.0
    assert result.data['net_income_loss'] == 18079.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 0.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 0.0
    assert result.data['income_before_equity_investments'] == 0.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 444075.0
    assert result.data['gross_profit'] == 104628.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 164278.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10K_Webfilings():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "goog-20131231.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 3755.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 0.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 38034.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == 0.0
    assert result.data['liabilities_and_equity'] == 110920.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 975.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 0.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 87309.0
    assert result.data['net_income_loss'] == 0.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 0.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 0.0
    assert result.data['income_before_equity_investments'] == 0.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 110920.0
    assert result.data['gross_profit'] == 0.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 72886.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10Q_Webfilings():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "goog-20140630.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 3683.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 913.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 11697.0
    assert result.data['non_current_assets'] == 43703.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == 3490.0
    assert result.data['liabilities_and_equity'] == 121608.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 0.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 95749.0
    assert result.data['net_income_loss'] == 3422.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 3579.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 3579.0
    assert result.data['income_before_equity_investments'] == 4403.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 121608.0
    assert result.data['gross_profit'] == 0.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 77905.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10Q_Rivet():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "c289-20140503.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 12535.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 14.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 708.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == -983.0
    assert result.data['liabilities_and_equity'] == 13261.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 3497.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 726.0
    assert result.data['net_income_loss'] == -983.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == -977.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == -977.0
    assert result.data['income_before_equity_investments'] == -969.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 13261.0
    assert result.data['gross_profit'] == 2687.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 10747.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10K_Rivet():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "rsh-20131231.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 234.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 42.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 583.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == -1914.0
    assert result.data['liabilities_and_equity'] == 15912.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 4445.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 2064.0
    assert result.data['net_income_loss'] == -1914.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == -1899.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == -1899.0
    assert result.data['income_before_equity_investments'] == -1872.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 15912.0
    assert result.data['gross_profit'] == 2784.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 13330.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10Q_QXInteractive():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "aaoi-20140630.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 5606.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 85.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 978.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == 1730.0
    assert result.data['liabilities_and_equity'] == 153524.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 9458.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 111781.0
    assert result.data['net_income_loss'] == 1919.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 2058.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 2058.0
    assert result.data['income_before_equity_investments'] == 0.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 153524.0
    assert result.data['gross_profit'] == 11188.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 106114.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10K_ThomsonReuters():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "aaoi-20131231.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 39057.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 0.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 177.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == -297.0
    assert result.data['liabilities_and_equity'] == 111057.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 6973.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 63077.0
    assert result.data['net_income_loss'] == -520.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 0.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 0.0
    assert result.data['income_before_equity_investments'] == 0.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 111057.0
    assert result.data['gross_profit'] == 6676.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 77936.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10Q_Fujitsu():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "aaww-20140630.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 233079.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == -23815.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 414512.0
    #assert result.data['non_current_assets'] == 3568474.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == 26657.0
    assert result.data['liabilities_and_equity'] == 4100064.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 4870.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 0.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 1355551.0
    assert result.data['net_income_loss'] == 0.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == -515.0
    assert result.data['equity_attributable_interest'] == 0.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == -515.0
    assert result.data['income_before_equity_investments'] == 0.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 4100064.0
    assert result.data['gross_profit'] == 0.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 531590.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10K_Fujitsu():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "aaww-20131231.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)
    print(result)

    assert result.data['liabilities'] == 194292.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 0.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 3124306.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == 0.0
    assert result.data['liabilities_and_equity'] == 3718259.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 4870.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 0.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 1317773.0
    assert result.data['net_income_loss'] == 0.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 0.0
    assert result.data['equity_attributable_interest'] == 4352.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 0.0
    assert result.data['income_before_equity_investments'] == 0.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    print(result.data['assets'])
    assert result.data['assets'] == 3718259.0
    assert result.data['gross_profit'] == 0.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 593953.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_income_loss_noncontrolling'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_GAAP10Q_Ez_XBRL():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "ggho-20140930.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                     str(file_to_parse
                                         .split("-")[1].split(".")[0][:4] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][4:6] +
                                         file_to_parse.split("-")[1]
                                         .split(".")[0][6:8]),
                                     "current")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)

    assert result.data['liabilities'] == 34273.0
    assert result.data['net_cash_flows_financing_continuing'] == 0.0
    assert result.data['revenue'] == 0.0
    assert result.data['income_tax_expense_benefit'] == 127.0
    assert result.data['income_from_equity_investments'] == 0.0
    assert result.data['preferred_stock_dividends'] == 0.0
    assert result.data['redeemable_noncontrolling_interest'] == 0.0
    assert result.data['extraordary_items_gain_loss'] == 0.0
    assert result.data['temporary_equity'] == 0.0
    assert result.data['costs_and_expenses'] == 0.0
    assert result.data['non_current_assets'] == 58615.0
    assert result.data['net_cash_flows_discontinued'] == 0.0
    assert result.data['income_loss'] == -7593.0
    assert result.data['liabilities_and_equity'] == 79451.0
    assert result.data['other_operating_income'] == 0.0
    assert result.data['operating_income_loss'] == 0.0
    assert result.data['net_income_parent'] == 0.0
    assert result.data['equity'] == 0.0
    assert result.data['net_cash_flows_operating_discontinued'] == 0.0
    assert result.data['cost_of_revenue'] == 0.0
    assert result.data['operating_expenses'] == 13026.0
    assert result.data['noncurrent_liabilities'] == 0.0
    assert result.data['current_liabilities'] == 0.0
    assert result.data['net_cash_flows_investing'] == 0.0
    assert result.data['stockholders_equity'] == 30543.0
    assert result.data['net_income_loss'] == -8642.0
    assert result.data['net_cash_flows_investing_continuing'] == 0.0
    assert result.data['nonoperating_income_loss'] == 0.0
    assert result.data['net_cash_flows_financing'] == 0.0
    assert result.data['net_income_shareholders'] == 0.0
    assert result.data['comprehensive_income'] == 0.0
    assert result.data['equity_attributable_interest'] == 309.0
    assert result.data['commitments_and_contingencies'] == 0.0
    assert result.data['comprehensive_income_parent'] == 0.0
    assert result.data['income_before_equity_investments'] == -8531.0
    assert result.data['comprehensive_income_interest'] == 0.0
    assert result.data['other_comprehensive_income'] == 0.0
    assert result.data['equity_attributable_parent'] == 0.0
    assert result.data['assets'] == 79451.0
    assert result.data['gross_profit'] == 5433.0
    assert result.data['net_cash_flows_operating_continuing'] == 0.0
    assert result.data['current_assets'] == 20836.0
    assert result.data['interest_and_debt_expense'] == 0.0
    assert result.data['net_cash_flows_operating'] == 0.0
    assert result.data['common_shares_outstanding'] == 0.0
    assert result.data['common_shares_issued'] == 0.0
    assert result.data['common_shares_authorized'] == 0.0


def test_parse_DEI10Q_RRDonnelley():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "sam-20130629.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    dei_obj = xbrl_parser.parseDEI(xbrl)

    serializer = DEISerializer()
    result = serializer.dump(dei_obj)

    assert result.data['trading_symbol'] == "SAM"
    assert result.data['company_name'] == "BOSTON BEER CO INC"
    assert result.data['shares_outstanding'] == 4007355.0
    assert result.data['public_float'] == 0.0


def test_parse_Custom10Q_RRDonnelley():

    xbrl_parser = XBRLParser(0)
    file_to_parse = "sam-20130629.xml"
    xbrl = xbrl_parser.parse(file_to_parse)
    custom_obj = xbrl_parser.parseCustom(xbrl)

    if six.PY3:

        result = len(custom_obj())

        assert result == 13

    if six.PY2 and not __pypy__:

        result = custom_obj()

        assert result[0] == ('conversionofclassbcommonstocktoclassacommonstockshares', '100000')
        assert result[1] == ('percentageofproductionvolumes', '0.90')
        assert result[2] == ('sharebasedcompensationarrangementbysharebasedpaymentawardoptionstovestineachtranche', '5000')
        assert result[3] == ('weightedaveragenumberofsharesoutstandingbasicincludingnonvestedparticipatingsecurities', '12866000')
        assert result[4] == ('incrementalcommonsharesattributabletoconversionofcommonstock', '4007000')
        assert result[5] == ('sharebasedcompensationarrangementbysharebasedpaymentawardinvestmentsharesweightedaveragegrantdat', '59.62')
        assert result[6] == ('incomeallocatedtoequityinstrumentsotherthanoptionnonvested', '7000')
        assert result[7] == ('netproceedsfromsaleofinvestmentshares', '531000')
        assert result[8] == ('weightedaveragenumberofbasicsharesoutstandingequityinstrumentsotherthanoptionnonvested', '94000')
        assert result[9] == ('sharebasedcompensationarrangementbysharebasedpaymentawardemployeeinvestmentsharespurchase', '12894')
        assert result[10] == ('provisionforreductionofdoubtfulaccounts', '-28000')
        assert result[11] == ('receiptofgovernmentgrantsforfacilitiesexpansion', '770000')
        assert result[12] == ('netincomelossallocatedtoequityinstrumentsotherthanoptionnonvested', '-143000')
