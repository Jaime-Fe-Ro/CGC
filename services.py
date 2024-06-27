import glob
import os

import pandas as pd

from constants import ACC_HIST_XLSX, PATH_FOLDER, ACC_HIST_DOWNLOAD_SHEET_AND_HEADERS

acc_data = {}


def get_old_acc_hist_data(account):
    acc_hist_xlsx = os.path.join(PATH_FOLDER + account + ACC_HIST_XLSX)
    xls = pd.ExcelFile(acc_hist_xlsx)

    old_data = {
        sheet_name: pd.read_excel(xls, sheet_name)
        for sheet_name in xls.sheet_names
    }

    return old_data


def update_db(old_data, new_data):
    get_data_diff(old_data, new_data)

    pass


def get_data_diff(old_data, new_data):
    assert old_data.columns.tolist() == new_data.columns.tolist()
    diff_df = pd.concat([old_data, new_data]).drop_duplicates(keep=False)
    print('diff_df', diff_df)
    return diff_df


def select_and_get_download(account):
    path = PATH_FOLDER + account
    xlsx_files = glob.glob(os.path.join('/', path, '*.xlsx'))
    filenames = [os.path.basename(file) for file in xlsx_files if '-' in os.path.basename(file)]
    return choose_download(account, filenames)


def choose_download(account, files):
    for file in files:
        print(f"{files.index(file) + 1}) {file}")
    file_selection = input("\nPor favor, seleccione un archivo -> ")
    selected_file_name = files[int(file_selection) - 1]

    return get_download_data(account, selected_file_name)


def get_download_data(account, download_doc_name):
    print('ACC_HIST_DOWNLOAD_SHEET_AND_HEADERS.items()', ACC_HIST_DOWNLOAD_SHEET_AND_HEADERS.items())
    for sheet, header in ACC_HIST_DOWNLOAD_SHEET_AND_HEADERS.items():
        print(f'Processing {sheet} with header {header}.')
        sheet_data = process_downloaded_sheet(account, download_doc_name, sheet, header)
        print(f'adding {sheet_data} to the acc_data dict.')
        acc_data.update(sheet_data)

    return acc_data


def process_downloaded_sheet(account, download_doc_name, sheet, headers):
    path = PATH_FOLDER + account + '/' + download_doc_name
    print(f'looking for {headers} in {sheet} in {download_doc_name} for account {account} in {path}.')
    xls = pd.ExcelFile(path)
    table_data = {}

    if isinstance(headers, list):
        print(f'headers {headers} is a list.')
        for header in headers:
            table_df = process_table(sheet, header, xls)
            table_data[header] = table_df
    else:
        print(f'headers {headers} is not a list.')
        table_df = process_table(sheet, headers, xls)
        table_data[headers] = table_df

    return table_data


def process_table(sheet, header, xls):
    df = pd.read_excel(xls, sheet_name=sheet)
    header_row, col_start = find_header_location(df, header)
    row_start = header_row + 1
    row_end, col_end = find_table_endpoints(df, row_start, col_start)
    print('----------------------------')
    print('header:', header)
    print('row_start, col_start:', row_start, col_start)
    print('row_end, col_end:', row_end, col_end)
    table_df = extract_table(df, row_start, col_start, row_end, col_end)
    return table_df


def find_header_location(df, header):
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            cell_value = df.iloc[row, col]
            if pd.isna(cell_value):
                continue
            if cell_value == header:
                return row, col
    raise KeyError(f"Header '{header}' not found in the DataFrame.")


def find_table_endpoints(df, row_start, col_start):
    print('df.shape:', df.shape)
    col = col_start
    while col < df.shape[1] and pd.notna(df.iat[row_start, col]):
        col += 1
    print('found last column:', col)
    col_end = col - 1

    row = row_start
    while row < df.shape[0] and pd.notna(df.iat[row, col_start]):
        row += 1
    print('found last row:', row)
    row_end = row - 1

    return row_end, col_end


def extract_table(df, row_start, col_start, row_end, col_end):
    return df.iloc[row_start:row_end, col_start:col_end]


# def save_new_data(account, xls):
#     global acc_data
#     new_data = {
#         sheet_name: pd.read_excel(xls, sheet_name)
#         for sheet_name in xls.sheet_names
#     }
#
#     for sheet, data in new_data.items():
#         if sheet in acc_data:
#             acc_data[sheet] = pd.concat([acc_data[sheet], data]).drop_duplicates().reset_index(drop=True)
#         else:
#             acc_data[sheet] = data
#
#     for sheet, data in acc_data.items():
#         print(f"Saving {sheet} for {account} with {len(data)} records.")
#
#     save_path = os.path.join(PATH_ACCOUNTS, account, "Historia completa actualizada.xlsx")
#     with pd.ExcelWriter(save_path) as writer:
#         for sheet_name, data in acc_data.items():
#             data.to_excel(writer, sheet_name=sheet_name, index=False)
#
#     print(f"Data saved to {save_path}")
