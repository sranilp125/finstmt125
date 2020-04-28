from finstmt.forecast.config import ForecastConfig, ForecastItemConfig
from finstmt.items.config import ItemConfig

# TODO [#3]: Better matching of financial statement item names - Balance Sheet
#
# Would be better to use regex instead of names list. Need to first add that infrastructure,
# then apply it to the Balance Sheet config.

# Note that each possible extract_name must be unique, it cannot be included in multiple lists
# Also note that all incoming names will be converted to lower case and stripped of punctuation,
# then split on _ and joined with space before matching these names
BALANCE_SHEET_INPUT_ITEMS = [
    ItemConfig(
        'cash',
        'Cash and Cash Equivalents',
        extract_names=[
            'cash',
            'cash and cash equivalents',
            'cash and equivalents',
            'cash and equiv',
            'cash cash equivalents',
            'cash equivalents',
            'cash equiv',
        ],
        forecast_config=ForecastItemConfig(
            plug=True
        )
    ),
    ItemConfig(
        'st_invest',
        'Short-Term Investments',
        extract_names=[
            'shortterm investments',
            'short term investments',
            'st investments',
            'shortterm invest',
            'short term invest',
            'st invest',
        ]
    ),
    ItemConfig(
        'cash_and_st_invest',
        'Cash and Short-Term Investments',
        extract_names=[
            'total cash st investments',
            'total cash and st investments',
            'total cash and shortterm investments',
            'total cash and short term investments',
            'total cash shortterm investments',
            'total cash short term investments',
            'total cash st invest',
            'total cash and st invest',
            'total cash and shortterm invest',
            'total cash and short term invest',
            'total cash shortterm invest',
            'total cash short term invest',
            'cash st investments',
            'cash and st investments',
            'cash and shortterm investments',
            'cash and short term investments',
            'cash shortterm investments',
            'cash short term investments',
            'cash st invest',
            'cash and st invest',
            'cash and shortterm invest',
            'cash and short term invest',
            'cash shortterm invest',
            'cash short term invest',
        ],
        expr_str='cash[t] + st_invest[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'receivables',
        'Receivables',
        extract_names=[
            'receivables',
            'rec',
            'accounts receivable',
            'ar'
        ],
        forecast_config=ForecastItemConfig(
            pct_of='revenue'
        )
    ),
    ItemConfig(
        'inventory',
        'Inventory',
        extract_names=[
            'inv',
            'inventory',
            'inventories'
        ],
        forecast_config=ForecastItemConfig(
            pct_of='revenue'
        )
    ),
    ItemConfig(
        'def_tax_st',
        'Deferred Tax Assets, Current',
        extract_names=[
            'def tax asset curr',
            'deferred tax asset curr',
            'tax asset curr',
            'def tax assets curr',
            'deferred tax assets curr',
            'tax assets curr',
            'def tax asset current',
            'deferred tax asset current',
            'tax asset current',
            'def tax assets current',
            'deferred tax assets current',
            'tax assets current',
            'def tax asset short term',
            'deferred tax asset short term',
            'tax asset short term',
            'def tax assets short term',
            'deferred tax assets short term',
            'tax assets short term',
            'def tax asset shortterm',
            'deferred tax asset shortterm',
            'tax asset shortterm',
            'def tax assets shortterm',
            'deferred tax assets shortterm',
            'tax assets shortterm',
            'def tax asset st',
            'deferred tax asset st',
            'tax asset st',
            'def tax assets st',
            'deferred tax assets st',
            'tax assets st',
        ]
    ),
    ItemConfig(
        'other_current_assets',
        'Other Current Assets',
        extract_names=[
            'other current assets',
            'other current asset',
            'other curr assets',
            'other curr asset',
            'oca',
        ]
    ),
    ItemConfig(
        'total_current_assets',
        'Total Current Assets',
        extract_names=[
            'total current assets',
            'tca',
        ],
        expr_str='cash_and_st_invest[t] + receivables[t] + inventory[t] + def_tax_st[t] + other_current_assets[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'gross_ppe',
        'Grosss Property, Plant & Equipment',
        extract_names=[
            'gross ppe',
            'gross property plant equipment',
            'gross property plant and equipment',
            'ppe gross',
            'property plant equipment gross',
            'property plant and equipment gross',
            'grs ppe',
            'grs property plant equipment',
            'grs property plant and equipment',
            'ppe grs',
            'property plant equipment grs',
            'property plant and equipment grs',
        ]
    ),
    ItemConfig(
        'dep',
        'Accumulated Depreciation',
        extract_names=[
            'accumulated depreciation',
            'depreciation',
            'dep',
            'accumulated dep',
            'acc depreciation',
            'accum depreciation',
            'acc dep',
            'accum dep',
        ]
    ),
    ItemConfig(
        'net_ppe',
        'Net Property, Plant & Equipment',
        extract_names=[
            'ppe',
            'property plant equipment',
            'property plant and equipment',
            'ppe net',
            'property plant equipment net',
            'property plant and equipment net',
            'net ppe',
            'net property plant equipment',
            'net property plant and equipment',
        ],
        expr_str='gross_ppe[t] - dep[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'goodwill',
        'Goodwill and Intangible Assets',
        extract_names=[
            'goodwill',
            'goodwill and intangible assets',
            'goodwill and intangibles',
            'goodwill intangible assets',
            'goodwill intangibles',
            'goodwill total',
            'goodwill and intangible assets total',
            'goodwill and intangibles total',
            'goodwill intangible assets total',
            'goodwill intangibles total',
        ]
        # TODO: need to be able to extract from multiple items at once
        #
        # Morningstar financial statements have Goodwill and then Intangibles other than Goodwill,
        # both of those should be coming into the Goodwill and Intagible Assets variable.
    ),
    ItemConfig(
        'lt_invest',
        'Long-Term Investments',
        extract_names=[
            'lt invest',
            'lt investments',
            'long term invest',
            'long term investments',
            'longterm invest',
            'longterm investments',
        ]
    ),
    ItemConfig(
        'def_tax_lt',
        'Deferred Tax Assets, Long-Term',
        extract_names=[
            'def tax asset long term',
            'deferred tax asset long term',
            'tax asset long term',
            'def tax assets long term',
            'deferred tax assets long term',
            'tax assets long term',
            'def tax asset longterm',
            'deferred tax asset longterm',
            'tax asset longterm',
            'def tax assets longterm',
            'deferred tax assets longterm',
            'tax assets longterm',
            'def tax asset lt',
            'deferred tax asset lt',
            'tax asset lt',
            'def tax assets lt',
            'deferred tax assets lt',
            'tax assets lt',
            'def tax asset',
            'deferred tax asset',
            'tax asset',
            'def tax assets',
            'deferred tax assets',
            'tax assets',
            'long term assets tax deferred',
            'lt assets tax deferred',
            'lt assets tax def',
            'long term assets tax def',
            'long term assets deferred tax',
            'lt assets deferred tax',
            'lt assets def tax',
            'long term assets def tax',
        ]
    ),
    ItemConfig(
        'other_lt_assets',
        'Other Long-Term Assets',
        extract_names=[
            'other lt assets',
            'other lt asset',
            'other longterm assets',
            'other longterm asset',
            'other long term assets',
            'other long term asset',
            'lt assets other',
            'lt asset other',
            'longterm assets other',
            'longterm asset other',
            'long term assets other',
            'long term asset other',
        ]
    ),
    ItemConfig(
        'total_non_current_assets',
        'Total Non-Current Assets',
        extract_names=[
            'total non current assets',
            'total noncurrent assets',
            'total lt assets',
            'total longterm assets',
            'total long term assets'
        ],
        expr_str='net_ppe[t] + goodwill[t] + lt_invest[t] + def_tax_lt[t] + other_lt_assets[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'total_assets',
        'Total Assets',
        extract_names=[
            'total assets',
            'total asset',
            'assets',
            'asset'
        ],
        expr_str='total_current_assets[t] + total_non_current_assets[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'payables',
        'Payables',
        extract_names=[
            'payables',
            'accounts payable',
            'ap',
            'payables and accrued expenses',
            'payables and accrued expense',
            'payable and accrued expenses',
            'payable and accrued expense',
            'payables and acc expenses',
            'payables and acc expense',
            'payable and acc expenses',
            'payable and acc expense',
            'payables and accrued exps',
            'payables and accrued exp',
            'payable and accrued exps',
            'payable and accrued exp',
            'payables and acc exps',
            'payables and acc exp',
            'payable and acc exps',
            'payable and acc exp',
        ],
        forecast_config=ForecastItemConfig(
            pct_of='revenue'
        )
    ),
    ItemConfig(
        'st_debt',
        'Short-Term Debt',
        extract_names=[
            'st debt',
            'short term debt',
            'shortterm debt',
            'st borrow',
            'short term borrow',
            'shortterm borrow'
            'st borrowings',
            'short term borrowings',
            'shortterm borrowings'
        ],
        forecast_config=ForecastItemConfig(
            pct_of='total_debt'
        )
    ),
    ItemConfig(
        'current_lt_debt',
        'Current Portion of Long-Term Debt',
        extract_names=[
            'curr port of lt debt',
            'curr port lt debt',
            'current port of lt debt',
            'current port lt debt',
            'curr portion of lt debt',
            'curr portion lt debt',
            'current portion of lt debt',
            'current portion lt debt',
            'curr port of longterm debt',
            'curr port longterm debt',
            'current port of longterm debt',
            'current port longterm debt',
            'curr portion of longterm debt',
            'curr portion longterm debt',
            'current portion of longterm debt',
            'current portion longterm debt',
            'curr port of long term debt',
            'curr port long term debt',
            'current port of long term debt',
            'current port long term debt',
            'curr portion of long term debt',
            'curr portion long term debt',
            'current portion of long term debt',
            'current portion long term debt',
            'curr port of debt',
            'curr port debt',
            'current port of debt',
            'current port debt',
            'curr portion of debt',
            'curr portion debt',
            'current portion of debt',
            'current portion debt',
            'curr part of lt debt',
            'curr part lt debt',
            'current part of lt debt',
            'current part lt debt',
            'curr part of longterm debt',
            'curr part longterm debt',
            'current part of longterm debt',
            'current part longterm debt',
            'curr part of long term debt',
            'curr part long term debt',
            'current part of long term debt',
            'current part long term debt',
            'curr part of debt',
            'curr part debt',
            'current part of debt',
            'current part debt',
        ],
        forecast_config=ForecastItemConfig(
            pct_of='total_debt'
        )
    ),
ItemConfig(
        'tax_liab_st',
        'Tax Liabilities, Short-Term',
        extract_names=[
            'tax liab shortterm',
            'tax liability shortterm',
            'tax liabilities shortterm',
            'tax liab short term',
            'tax liability short term',
            'tax liabilities short term',
            'tax liab st',
            'tax liability st',
            'tax liabilities st',
            'shortterm tax liab',
            'shortterm tax liability',
            'shortterm tax liabilities',
            'short term tax liab',
            'short term tax liability',
            'short term tax liabilities',
            'st tax liab',
            'st tax liability',
            'st tax liabilities',
            'def tax liab shortterm',
            'def tax liability shortterm',
            'def tax liabilities shortterm',
            'def tax liab short term',
            'def tax liability short term',
            'def tax liabilities short term',
            'def tax liab st',
            'def tax liability st',
            'def tax liabilities st',
            'def shortterm tax liab',
            'def shortterm tax liability',
            'def shortterm tax liabilities',
            'def short term tax liab',
            'def short term tax liability',
            'def short term tax liabilities',
            'def st tax liab',
            'def st tax liability',
            'def st tax liabilities',
            'deferred tax liab shortterm',
            'deferred tax liability shortterm',
            'deferred tax liabilities shortterm',
            'deferred tax liab short term',
            'deferred tax liability short term',
            'deferred tax liabilities short term',
            'deferred tax liab st',
            'deferred tax liability st',
            'deferred tax liabilities st',
            'deferred shortterm tax liab',
            'deferred shortterm tax liability',
            'deferred shortterm tax liabilities',
            'deferred short term tax liab',
            'deferred short term tax liability',
            'deferred short term tax liabilities',
            'deferred st tax liab',
            'deferred st tax liability',
            'deferred st tax liabilities',
            'tax liab noncurr',
            'tax liability noncurr',
            'tax liabilities noncurr',
            'tax liab non curr',
            'tax liability non curr',
            'tax liabilities non curr',
            'noncurr tax liab',
            'noncurr tax liability',
            'noncurr tax liabilities',
            'non curr tax liab',
            'non curr tax liability',
            'non curr tax liabilities',
            'def tax liab noncurr',
            'def tax liability noncurr',
            'def tax liabilities noncurr',
            'def tax liab non curr',
            'def tax liability non curr',
            'def tax liabilities non curr',
            'def noncurr tax liab',
            'def noncurr tax liability',
            'def noncurr tax liabilities',
            'def non curr tax liab',
            'def non curr tax liability',
            'def non curr tax liabilities',
            'deferred tax liab noncurr',
            'deferred tax liability noncurr',
            'deferred tax liabilities noncurr',
            'deferred tax liab non curr',
            'deferred tax liability non curr',
            'deferred tax liabilities non curr',
            'deferred noncurr tax liab',
            'deferred noncurr tax liability',
            'deferred noncurr tax liabilities',
            'deferred non curr tax liab',
            'deferred non curr tax liability',
            'deferred non curr tax liabilities',
            'tax liab noncurrent',
            'tax liability noncurrent',
            'tax liabilities noncurrent',
            'tax liab non current',
            'tax liability non current',
            'tax liabilities non current',
            'noncurrent tax liab',
            'noncurrent tax liability',
            'noncurrent tax liabilities',
            'non current tax liab',
            'non current tax liability',
            'non current tax liabilities',
            'def tax liab noncurrent',
            'def tax liability noncurrent',
            'def tax liabilities noncurrent',
            'def tax liab non current',
            'def tax liability non current',
            'def tax liabilities non current',
            'def noncurrent tax liab',
            'def noncurrent tax liability',
            'def noncurrent tax liabilities',
            'def non current tax liab',
            'def non current tax liability',
            'def non current tax liabilities',
            'deferred tax liab noncurrent',
            'deferred tax liability noncurrent',
            'deferred tax liabilities noncurrent',
            'deferred tax liab non current',
            'deferred tax liability non current',
            'deferred tax liabilities non current',
            'deferred noncurrent tax liab',
            'deferred noncurrent tax liability',
            'deferred noncurrent tax liabilities',
            'deferred non current tax liab',
            'deferred non current tax liability',
            'deferred non current tax liabilities',
        ]
    ),
    ItemConfig(
        'other_current_liab',
        'Other Current Liabilities',
        extract_names=[
            'other current liabilities',
            'other current liab',
            'other curr liabilities',
            'other curr liab',
            'other liabilities current',
            'other liab current',
            'other liabilities curr',
            'other liab curr',
        ]
    ),
    ItemConfig(
        'total_current_liab',
        'Total Current Liabilities',
        extract_names=[
            'total current liabilities',
        ],
        expr_str='payables[t] + st_debt[t] + tax_liab_st[t] + current_lt_debt[t] + other_current_liab[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'lt_debt',
        'Long-Term Debt',
        extract_names=[
            'lt debt',
            'long term debt',
            'longterm debt',
            'lt borrow',
            'long term borrow',
            'longterm borrow',
            'lt borrowings',
            'long term borrowings',
            'longterm borrowings',
            'lt debt total',
            'long term debt total',
            'longterm debt total',
            'lt borrow total',
            'long term borrow total',
            'longterm borrow total',
            'lt borrowings total',
            'long term borrowings total',
            'longterm borrowings total',
        ],
        forecast_config=ForecastItemConfig(
            plug=True
        )
    ),
    ItemConfig(
        'total_debt',
        'Total Debt',
        extract_names=[
            'total debt'
        ],
        expr_str='st_debt[t] + lt_debt[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'deferred_rev',
        'Deferred Revenue',
        extract_names=[
            'deferred revenue',
            'deferred sales',
            'def revenue',
            'def sales'
            'non current revenue',
            'non current sales',
            'non current revenue def',
            'non current sales def',
            'non current revenue deferred',
            'non current sales deferred',
            'revenue non current',
            'sales non current',
            'revenue def non current',
            'sales def non current',
            'revenue deferred non current',
            'sales deferred non current',
            'def revenue non current',
            'def sales non current',
            'def revenue def non current',
            'def sales def non current',
            'def revenue deferred non current',
            'def sales deferred non current',
            'deferred revenue non current',
            'deferred sales non current',
            'deferred revenue def non current',
            'deferred sales def non current',
            'deferred revenue deferred non current',
            'deferred sales deferred non current',
            'non curr revenue',
            'non curr sales',
            'non curr revenue def',
            'non curr sales def',
            'non curr revenue deferred',
            'non curr sales deferred',
            'revenue non curr',
            'sales non curr',
            'revenue def non curr',
            'sales def non curr',
            'revenue deferred non curr',
            'sales deferred non curr',
            'def revenue non curr',
            'def sales non curr',
            'def revenue def non curr',
            'def sales def non curr',
            'def revenue deferred non curr',
            'def sales deferred non curr',
            'deferred revenue non curr',
            'deferred sales non curr',
            'deferred revenue def non curr',
            'deferred sales def non curr',
            'deferred revenue deferred non curr',
            'deferred sales deferred non curr'
            'noncurrent revenue',
            'noncurrent sales',
            'noncurrent revenue def',
            'noncurrent sales def',
            'noncurrent revenue deferred',
            'noncurrent sales deferred',
            'revenue noncurrent',
            'sales noncurrent',
            'revenue def noncurrent',
            'sales def noncurrent',
            'revenue deferred noncurrent',
            'sales deferred noncurrent',
            'def revenue noncurrent',
            'def sales noncurrent',
            'def revenue def noncurrent',
            'def sales def noncurrent',
            'def revenue deferred noncurrent',
            'def sales deferred noncurrent',
            'deferred revenue noncurrent',
            'deferred sales noncurrent',
            'deferred revenue def noncurrent',
            'deferred sales def noncurrent',
            'deferred revenue deferred noncurrent',
            'deferred sales deferred noncurrent',
            'noncurr revenue',
            'noncurr sales',
            'noncurr revenue def',
            'noncurr sales def',
            'noncurr revenue deferred',
            'noncurr sales deferred',
            'revenue noncurr',
            'sales noncurr',
            'revenue def noncurr',
            'sales def noncurr',
            'revenue deferred noncurr',
            'sales deferred noncurr',
            'def revenue noncurr',
            'def sales noncurr',
            'def revenue def noncurr',
            'def sales def noncurr',
            'def revenue deferred noncurr',
            'def sales deferred noncurr',
            'deferred revenue noncurr',
            'deferred sales noncurr',
            'deferred revenue def noncurr',
            'deferred sales def noncurr',
            'deferred revenue deferred noncurr',
            'deferred sales deferred noncurr'
        ]
    ),
    ItemConfig(
        'tax_liab_lt',
        'Tax Liabilities, Long-Term',
        extract_names=[
            'tax liab longterm',
            'tax liability longterm',
            'tax liabilities longterm',
            'tax liab long term',
            'tax liability long term',
            'tax liabilities long term',
            'tax liab lt',
            'tax liability lt',
            'tax liabilities lt',
            'longterm tax liab',
            'longterm tax liability',
            'longterm tax liabilities',
            'long term tax liab',
            'long term tax liability',
            'long term tax liabilities',
            'lt tax liab',
            'lt tax liability',
            'lt tax liabilities',
            'tax liab longterm def',
            'tax liability longterm def',
            'tax liabilities longterm def',
            'tax liab long term def',
            'tax liability long term def',
            'tax liabilities long term def',
            'tax liab lt def',
            'tax liability lt def',
            'tax liabilities lt def',
            'longterm tax liab def',
            'longterm tax liability def',
            'longterm tax liabilities def',
            'long term tax liab def',
            'long term tax liability def',
            'long term tax liabilities def',
            'lt tax liab def',
            'lt tax liability def',
            'lt tax liabilities def',
            'tax liab longterm deferred',
            'tax liability longterm deferred',
            'tax liabilities longterm deferred',
            'tax liab long term deferred',
            'tax liability long term deferred',
            'tax liabilities long term deferred',
            'tax liab lt deferred',
            'tax liability lt deferred',
            'tax liabilities lt deferred',
            'longterm tax liab deferred',
            'longterm tax liability deferred',
            'longterm tax liabilities deferred',
            'long term tax liab deferred',
            'long term tax liability deferred',
            'long term tax liabilities deferred',
            'lt tax liab deferred',
            'lt tax liability deferred',
            'lt tax liabilities deferred',
            'def tax liab longterm',
            'def tax liability longterm',
            'def tax liabilities longterm',
            'def tax liab long term',
            'def tax liability long term',
            'def tax liabilities long term',
            'def tax liab lt',
            'def tax liability lt',
            'def tax liabilities lt',
            'def longterm tax liab',
            'def longterm tax liability',
            'def longterm tax liabilities',
            'def long term tax liab',
            'def long term tax liability',
            'def long term tax liabilities',
            'def lt tax liab',
            'def lt tax liability',
            'def lt tax liabilities',
            'deferred tax liab longterm',
            'deferred tax liability longterm',
            'deferred tax liabilities longterm',
            'deferred tax liab long term',
            'deferred tax liability long term',
            'deferred tax liabilities long term',
            'deferred tax liab lt',
            'deferred tax liability lt',
            'deferred tax liabilities lt',
            'deferred longterm tax liab',
            'deferred longterm tax liability',
            'deferred longterm tax liabilities',
            'deferred long term tax liab',
            'deferred long term tax liability',
            'deferred long term tax liabilities',
            'deferred lt tax liab',
            'deferred lt tax liability',
            'deferred lt tax liabilities',
            'tax liab noncurrent',
            'tax liability noncurrent',
            'tax liabilities noncurrent',
            'noncurrent tax liab',
            'noncurrent tax liability',
            'noncurrent tax liabilities',
            'def tax liab noncurrent',
            'def tax liability noncurrent',
            'def tax liabilities noncurrent',
            'def noncurrent tax liab',
            'def noncurrent tax liability',
            'def noncurrent tax liabilities',
            'deferred tax liab noncurrent',
            'deferred tax liability noncurrent',
            'deferred tax liabilities noncurrent',
            'deferred noncurrent tax liab',
            'deferred noncurrent tax liability',
            'deferred noncurrent tax liabilities',
            'tax liab noncurr',
            'tax liability noncurr',
            'tax liabilities noncurr',
            'noncurr tax liab',
            'noncurr tax liability',
            'noncurr tax liabilities',
            'def tax liab noncurr',
            'def tax liability noncurr',
            'def tax liabilities noncurr',
            'def noncurr tax liab',
            'def noncurr tax liability',
            'def noncurr tax liabilities',
            'deferred tax liab noncurr',
            'deferred tax liability noncurr',
            'deferred tax liabilities noncurr',
            'deferred noncurr tax liab',
            'deferred noncurr tax liability',
            'deferred noncurr tax liabilities',
            'tax liab non current',
            'tax liability non current',
            'tax liabilities non current',
            'non current tax liab',
            'non current tax liability',
            'non current tax liabilities',
            'def tax liab non current',
            'def tax liability non current',
            'def tax liabilities non current',
            'def non current tax liab',
            'def non current tax liability',
            'def non current tax liabilities',
            'deferred tax liab non current',
            'deferred tax liability non current',
            'deferred tax liabilities non current',
            'deferred non current tax liab',
            'deferred non current tax liability',
            'deferred non current tax liabilities',
            'tax liab non curr',
            'tax liability non curr',
            'tax liabilities non curr',
            'non curr tax liab',
            'non curr tax liability',
            'non curr tax liabilities',
            'def tax liab non curr',
            'def tax liability non curr',
            'def tax liabilities non curr',
            'def non curr tax liab',
            'def non curr tax liability',
            'def non curr tax liabilities',
            'deferred tax liab non curr',
            'deferred tax liability non curr',
            'deferred tax liabilities non curr',
            'deferred non curr tax liab',
            'deferred non curr tax liability',
            'deferred non curr tax liabilities',
            'tax liab',
            'tax liability',
            'tax liabilities'
        ]
    ),
    ItemConfig(
        'deposit_liab',
        'Deposit Liabilities',
        extract_names=[
            'deposit liab',
            'deposit liability',
            'deposit liabilities',
        ]
    ),
    ItemConfig(
        'other_lt_liab',
        'Other Long-Term Liabilities',
        extract_names=[
            'other lt liabilities',
            'other longterm liabilities',
            'other long term liabilities',
            'other lt liab',
            'other longterm liab',
            'other long term liab',
            'other noncurrent liabilities',
            'other non current liabilities',
            'other noncurr liabilities',
            'other non curr liabilities',
            'other noncurrent liab',
            'other non current liab',
            'other noncurr liab',
            'other non curr liab',
            'other liabilities lt',
            'other liabilities longterm',
            'other liabilities long term',
            'other liab lt',
            'other liab longterm',
            'other liab long term',
            'other liabilities noncurrent',
            'other liabilities non current',
            'other liabilities noncurr',
            'other liabilities non curr',
            'other liab noncurrent',
            'other liab non current',
            'other liab noncurr',
            'other liab non curr',
            'lt liabilities other',
            'longterm liabilities other',
            'long term liabilities other',
            'lt liab other',
            'longterm liab other',
            'long term liab other',
            'noncurrent liabilities other',
            'non current liabilities other',
            'noncurr liabilities other',
            'non curr liabilities other',
            'noncurrent liab other',
            'non current liab other',
            'noncurr liab other',
            'non curr liab other',
            'liabilities lt other',
            'liabilities longterm other',
            'liabilities long term other',
            'liab lt other',
            'liab longterm other',
            'liab long term other',
            'liabilities noncurrent other',
            'liabilities non current other',
            'liabilities noncurr other',
            'liabilities non curr other',
            'liab noncurrent other',
            'liab non current other',
            'liab noncurr other',
            'liab non curr other',
        ]
    ),
    ItemConfig(
        'total_non_current_liab',
        'Total Non-Current Liabilities',
        extract_names=[
            'total non current liabilities',
            'total noncurrent liabilities',
            'total non current liability',
            'total noncurrent liability',
            'total non current liab',
            'total noncurrent liab',
        ],
        expr_str='lt_debt[t] + deferred_rev[t] + tax_liab_lt[t] + deposit_liab[t] + other_lt_liab[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'total_liab',
        'Total Liabilities',
        extract_names=[
            'total liab',
            'total liability',
            'total liabilities',
        ],
        expr_str='total_non_current_liab[t] + total_current_liab[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'common_stock',
        'Common Stock',
        extract_names=[
            'total common stock',
            'total stock',
            'total common shares',
            'total shares',
            'common stock',
            'stock'
            'common shares',
            'shares',
            'net total common stock',
            'net total stock',
            'net total common shares',
            'net total shares',
            'net common stock',
            'net stock'
            'net common shares',
            'net shares',
            'total common stock net',
            'total stock net',
            'total common shares net',
            'total shares net',
            'common stock net',
            'stock net'
            'common shares net',
            'shares net'
        ]
    ),
    ItemConfig(
        'other_income',
        'Other Comprehensive Income',
        extract_names=[
            'other income',
            'other comprehensive income',
            'other comp income',
            'comp income',
            'comprehensive income',
            'comprehensive income and other',
            'comp income and other',
            'comp inc and other',
            'comprehensive inc and other',
            'comprehensive income other',
            'comp income other',
            'comp inc other',
            'comprehensive inc other',
        ],
        force_positive=False
    ),
    ItemConfig(
        'retained_earnings',
        'Retained Earnings',
        extract_names=[
            're',
            'retained earnings',
            'retained earnings deficit',
            're deficit'
        ],
        # TODO [#4]: forecast of retained earnings should be calculated
        #
        # Should be a calculation of retained_earnings[t-1] + net income[t] - dividends[t]
    ),
    ItemConfig(
        'minority_interest',
        'Minority Interest',
        extract_names=[
            'minority interest',
            'minority int',
            'min int',
            'min interest',
        ]
    ),
    ItemConfig(
        'total_equity',
        "Total Stockholder's Equity",
        extract_names=[
            'total equity',
            'total shareholders equity',
            'total stockholders equity',
            'equity total',
            'shareholders equity total',
            'stockholders equity total',
            'equity',
            'shareholders equity',
            'stockholders equity',
        ],
        expr_str='other_income[t] + retained_earnings[t] + common_stock[t] + minority_interest[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        'total_liab_and_equity',
        'Total Liabilities and Equity',
        extract_names=[
            'total liabilities and equity',
            'total liab and equity',
            'total liabilities equity',
            'total liab equity',
            'liabilities and equity',
            'liab and equity',
            'liabilities equity',
            'liab equity',
        ],
        expr_str='total_liab[t] + total_equity[t]',
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    )
]