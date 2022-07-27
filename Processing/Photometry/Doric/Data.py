# Import
import csv
import numpy as np
import pandas as pd
from Processing.Photometry import Filters


# Functions


class NeuralData:
    def __init__(self, path):
        self.ttl_name = None
        self.act_name = None
        self.iso_name = None
        self.time_name = None
        self.data_act = None
        self.data_iso = None
        self.time_data = None
        self.condensed_dataset = None
        doric_file = open(path)
        doric_csv_reader = csv.reader(doric_file)
        doric_name_list = list()
        doric_list = list()
        for row in doric_csv_reader:
            if row[0].isdigit():
                row[0] = float(row[0])
            if isinstance(row[0], float):
                doric_list.append(row)
            elif isinstance(row[0], str):
                doric_name_list = row
            elif row[0] == '':
                break
            else:
                continue
        doric_file.close()
        doric_numpy = np.array(doric_list)
        self.main_dataset = pd.DataFrame(data=doric_numpy, columns=doric_name_list)
        self.main_dataset = self.main_dataset.astype('float')

    def select_cols(self, time_name, iso_name, act_name, ttl_name):
        self.time_name = time_name
        self.iso_name = iso_name
        self.act_name = act_name
        self.ttl_name = ttl_name
        self.condensed_dataset = self.main_dataset[[self.time_name, self.iso_name, self.act_name, self.ttl_name]]

    def report_cols(self):
        return self.main_dataset.columns

    def time_sync(self,sync_value):
        self.condensed_dataset[self.time_name] = self.condensed_dataset[self.time_name] - sync_value

    def cut_negative_time(self):
        self.condensed_dataset = self.condensed_dataset[self.condensed_dataset[self.time_name] >= 0]

    def filter_data(self, filter_type, order, **kwargs):
        if filter_type == 'butterworth':
            self.data_iso, self.data_act = Filters.butterworth(time_data=self.time_data, data_iso=self.data_iso,
                                                               data_act=self.data_act, order=order,
                                                               filter_freq=kwargs['filter_freq'],
                                                               filt_type=kwargs['filt_type'], analog=kwargs['analog'])
