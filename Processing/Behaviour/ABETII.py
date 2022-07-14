# Imports
import os
import sys
import csv
import numpy as np
import pandas as pd


# Class - ABET II Object
class BehaviourData:
    def __init__(self, path):
        self.trial_definition_times = None
        self.event_name = None
        self.event_times = None
        self.curr_dir = os.getcwd()
        if sys.platform == 'linux' or sys.platform == 'darwin':
            self.folder_symbol = '/'
        elif sys.platform == 'win32':
            self.folder_symbol = '\\'
        self.main_folder_path = os.getcwd()
        self.data_folder_path = self.main_folder_path + self.folder_symbol + 'Data' + self.folder_symbol

        self.extra_prior = 0
        self.extra_follow = 0

        abet_file = open(path)
        abet_csv_reader = csv.reader(abet_file)
        abet_data_list = list()
        abet_name_list = list()
        event_time_colname = ['Evnt_Time', 'Event_Time']
        colnames_found = False
        for row in abet_csv_reader:
            if not colnames_found:
                if len(row) == 0:
                    continue
                if row[0] == 'Animal ID':
                    self.animal_id = str(row[1])
                    continue
                if row[0] == 'Date/Time':
                    self.date = str(row[1])
                    self.date = self.date.replace(':', '-')
                    self.date = self.date.replace('/', '-')
                    continue
                if row[0] in event_time_colname:
                    colnames_found = True
                    self.time_var_name = row[0]
                    self.event_name_col = row[2]
                    abet_name_list = [row[0], row[1], row[2], row[3], row[5], row[8]]
                else:
                    continue
            else:
                abet_data_list.append([row[0], row[1], row[2], row[3], row[5], row[8]])
        abet_file.close()
        abet_numpy = np.array(abet_data_list)
        self.main_dataset = pd.DataFrame(data=abet_numpy, columns=abet_name_list)

    def search_event(self, start_event_id='1', start_event_group='', start_event_item_name='',
                     start_event_position=None, filter_list=None, extra_prior_time=0, extra_follow_time=0,
                     exclusion_list=None):

        if exclusion_list is None:
            exclusion_list = []
        if filter_list is None:
            filter_list = []
        if start_event_position is None:
            start_event_position = ['']

        def filter_event(event_data, abet_data, filter_type='', filter_name='', filter_group='', filter_arg='',
                         filter_before=''):
            condition_event_names = ['Condition Event']
            variable_event_names = ['Variable Event']
            if filter_type in condition_event_names:
                filter_event_abet = abet_data.loc[(abet_data[self.event_name_col] == str(filter_type)) & (
                        abet_data['Group_ID'] == str(int(filter_group))), :]
                filter_event_abet = filter_event_abet[~filter_event_abet.isin(exclusion_list)]
                filter_event_abet = filter_event_abet.dropna(subset=['Item_Name'])
                for index, value in event_data.items():
                    sub_values = filter_event_abet.loc[:, self.time_var_name]
                    sub_values = sub_values.astype(dtype='float64')
                    sub_values = sub_values.sub(float(value))
                    filter_before = int(float(filter_before))
                    if filter_before == 1:
                        sub_values[sub_values > 0] = np.nan
                    elif filter_before == 0:
                        sub_values[sub_values < 0] = np.nan
                    sub_index = sub_values.abs().idxmin(skipna=True)
                    sub_null = sub_values.isnull().sum()
                    if sub_null >= sub_values.size:
                        continue

                    filter_value = filter_event_abet.loc[sub_index, 'Item_Name']
                    if filter_value != filter_name:
                        event_data[index] = np.nan

                event_data = event_data.dropna()
                event_data = event_data.reset_index(drop=True)
            elif filter_type in variable_event_names:
                filter_event_abet = abet_data.loc[(abet_data[self.event_name_col] == str(filter_type)) & (
                        abet_data['Item_Name'] == str(filter_name)), :]
                filter_event_abet = filter_event_abet[~filter_event_abet.isin(exclusion_list)]
                filter_event_abet = filter_event_abet.dropna(subset=['Item_Name'])
                for index, value in event_data.items():
                    sub_values = filter_event_abet.loc[:, self.time_var_name]
                    sub_values = sub_values.astype(dtype='float64')
                    sub_values = sub_values.sub(float(value))
                    sub_null = sub_values.isnull().sum()
                    filter_before = int(float(filter_before))
                    if sub_null >= sub_values.size:
                        continue
                    if filter_before == 1:
                        sub_values[sub_values > 0] = np.nan
                    elif filter_before == 0:
                        sub_values[sub_values < 0] = np.nan
                    sub_index = sub_values.abs().idxmin(skipna=True)

                    filter_value = filter_event_abet.loc[sub_index, 'Arg1_Value']
                    if float(filter_value) != float(filter_arg):
                        event_data[index] = np.nan

                event_data = event_data.dropna()
                event_data = event_data.reset_index(drop=True)
            return event_data

        touch_event_names = ['Touch Up Event', 'Touch Down Event', 'Whisker - Clear Image by Position']

        if start_event_id in touch_event_names:
            filtered_abet = self.main_dataset.loc[(self.main_dataset[self.event_name_col] == str(start_event_id)) &
                                                  (self.main_dataset['Group_ID'] == str(start_event_group)) &
                                                  (self.main_dataset['Item_Name'] == str(start_event_item_name)) &
                                                  (self.main_dataset['Arg1_Value'] == str(start_event_position)), :]

        else:
            filtered_abet = self.main_dataset.loc[(self.main_dataset[self.event_name_col] == str(start_event_id)) & (
                    self.main_dataset['Group_ID'] == str(start_event_group)) &
                                                 (self.main_dataset['Item_Name'] == str(start_event_item_name)), :]

        self.event_times = filtered_abet.loc[:, self.time_var_name]
        self.event_times = self.event_times.reset_index(drop=True)
        self.event_times = pd.to_numeric(self.event_times, errors='coerce')

        if filter_event:
            for fil in filter_list:
                self.event_times = filter_event(self.event_times, self.main_dataset, str(fil['Type']), str(fil['Name']),
                                                str(fil['Group']), str(fil['Arg']), str(fil['Prior']))

        abet_start_times = self.event_times - extra_prior_time
        abet_end_times = self.event_times + extra_follow_time
        self.event_times = pd.concat([abet_start_times, abet_end_times], axis=1)
        self.event_times.columns = ['Start_Time', 'End_Time']
        self.event_name = start_event_item_name
        self.extra_follow = extra_follow_time
        self.extra_prior = extra_prior_time

    def trial_definition(self, start_event_group, end_event_group):
        if not isinstance(start_event_group, list):
            return "Start event not in list"
        if not isinstance(end_event_group, list):
            return "End Event not in list"

        event_group_list = start_event_group + end_event_group
        filtered_abet = self.main_dataset[self.main_dataset.Item_Name.isin(event_group_list)]
        filtered_abet = filtered_abet.reset_index(drop=True)
        if filtered_abet.iloc[0, 3] not in start_event_group:
            filtered_abet = filtered_abet.drop([0])  # OCCURS IF FIRST INSTANCE IS THE END OF A TRIAL (COMMON WITH ITI)
        trial_times = filtered_abet.loc[:, self.time_var_name]
        trial_times = trial_times.reset_index(drop=True)
        start_times = trial_times.iloc[::2]
        start_times = start_times.reset_index(drop=True)
        start_times = pd.to_numeric(start_times, errors='coerce')
        end_times = trial_times.iloc[1::2]
        end_times = end_times.reset_index(drop=True)
        end_times = pd.to_numeric(end_times, errors='coerce')
        self.trial_definition_times = pd.concat([start_times, end_times], axis=1)
        self.trial_definition_times.columns = ['Start_Time', 'End_Time']
        self.trial_definition_times = self.trial_definition_times.reset_index(drop=True)
