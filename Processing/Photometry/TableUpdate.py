# Import
import csv

# Table Update Information


def table_update(data_type):
    if data_type == 'Doric Photometry Data':
        num_new_cols = 3
        new_col_types = ['combobox','combobox','combobox']
        new_col_labels = ['Isobestic Column','Active Column','TTL Column']
        new_col_spaces = [100,100,100]
        new_col_dict = {'num_col':num_new_cols,'col_type':new_col_types,'col_label':new_col_labels,'col_space':new_col_spaces}

    return new_col_dict

def set_doric_combobox_values(doric_file):
    doric_data = open(doric_file)
    doric_csv_reader = csv.reader(doric_data)
    row_read = 0
    for row in doric_csv_reader:
        if row_read == 0:
            first_col = row
        elif row_read == 1:
            second_col = row
        elif row_read >= 2:
            break
        row_read += 1
    doric_data.close()

    if isinstance(row[0],str):
        return second_col
    else:
        return first_col
