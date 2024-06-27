import os

ACC_LIST = ['J+M', 'JF', 'P+J+M']  # List of accounts TODO: Change this to function that looks for accounts in folder

PATH_CONSTANTS = (os.path.abspath(__file__)).replace("\\", "/")
#  PATH_CONSTANTS: C:/Users/jaime/OneDrive/Stock market/Stock market accounts/CGC/constants.py
PATH_FOLDER = os.path.dirname(PATH_CONSTANTS) + '/'
#  PATH_FOLDER: C:/Users/jaime/OneDrive/Stock market/Stock market accounts/CGC/
PATH_ACCOUNTS = os.path.dirname(os.path.dirname(PATH_FOLDER)) + '/'
#  PATH_ACCOUNTS: C:/Users/jaime/OneDrive/Stock market/Stock market accounts/
ACC_HIST_XLSX = '/Historia completa.xlsx'

ACC_HIST_SHEET_AND_TABLE_NAMES = {
    'Balance': 'Balance',
    'Trade History': 'Trade_History',
    'Orders History': 'Orders_History',
    'Withdrawal Deposit Details': 'Withdrawal_Deposit_Details',
    'Commisions & Fees': 'Commisions_Fees'
}

ACC_HIST_ORDER_DOWNLOAD_HEADERS = ['Balance', 'Trade History', 'Orders History']
ACC_HIST_DOWNLOAD_SHEET_AND_HEADERS = {
    'Orders': ACC_HIST_ORDER_DOWNLOAD_HEADERS,
    'Withdrawal Deposit Details': 'Withdrawal/Deposit Details',
    'Commisions & Fees': 'Commisions & Fees'
}

KEY_MAPPING = {
    'Balance': 'Balance',
    'Trade History': 'Trade History',
    'Orders History': 'Orders History',
    'Withdrawal Deposit Details': 'Withdrawal/Deposit Details',
    'Commisions & Fees': 'Commisions & Fees'
}

# ACC_POSITION_STORAGE_SHEET_AND_TABLE_NAMES = {
#     'Shares': 'Shares',
#     'Options': 'Options'
#     }
