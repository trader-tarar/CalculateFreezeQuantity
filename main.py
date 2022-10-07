#The below code fetches the Freeze Quantity for an input symbol from NSE.
# Enter NIFTY for NIFTY
#BANKNIFTY for BANKNIFTY

import pandas as pd

def calcFreezeQuantity(symbol):
    try:
        qty_freeze_df = pd.read_excel('https://archives.nseindia.com/content/fo/qtyfreeze.xls', )
    except Exception as e:
        print('Exception occured while fetching the Freeze Quantity Data from NSE.')
        exit(0)
    else:
        listOfColumns = qty_freeze_df.columns
        strippedListOfColumns = []

        for i in listOfColumns:
            strippedListOfColumns.append(i.strip())

        qty_freeze_df.columns = strippedListOfColumns

        listOfSymbols = qty_freeze_df.SYMBOL.to_list()
        strippedListOfSymbols = []

        for i in listOfSymbols:
            strippedListOfSymbols.append(i.strip())

        qty_freeze_df['SYMBOL'] = strippedListOfSymbols
        qty_freeze = qty_freeze_df[qty_freeze_df['SYMBOL'] == symbol].iloc[0]['VOL_FRZ_QTY']
        return qty_freeze

symbol = input('Please enter the Symbol for which the Freeze Quantity is to be calculated: (Fro ex. NIFTY or BANKNIFTY):\r\n')
symbol = symbol.upper()
freeze_quanity_for_a_symobl = calcFreezeQuantity(symbol)
print(f'The freeze quantity for the {symbol} is {freeze_quanity_for_a_symobl}')

#you can use the variable which is of type numpy.int64 in your code.