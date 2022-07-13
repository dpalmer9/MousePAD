# Import
import csv
import numpy as np
import pandas as pd

# Functions


class NeuralData:
    def __init__(self,path):
        doric_file = open(path)
        doric_csv_reader = csv.reader(doric_file)
        first_row_read = False
        second_row_read = False
        doric_name_list = list()
        doric_list = list()
        for row in doric_csv_reader:
            try:
                row[0] = float(row[0])
            except:
                continue
            if isinstance(row[0], float):
                doric_list.append(row)
            elif isinstance(row[0],str):
                doric_name_list = row
            elif row[0] == '':
                break
            else:
                continue
        doric_file.close()
        doric_numpy = np.array(doric_list)
        self.doric_pandas = pd.DataFrame(data=doric_numpy, columns=doric_name_list)
        self.doric_pandas = self.doric_pandas.astype('float')