# Import
import numpy as np
import pandas as pd
import csv

# Functions


def read_data(file_path):
    abet_file = open(file_path)
    abet_csv_reader = csv.reader(abet_file)
    abet_data_list = list()
    abet_name_list = list()
    abet_data_colname = list()
    animal_descriptive_dictionary = dict()
    event_time_colname = ['Evnt_Time', 'Event_Time']
    colname_detected = False

    for row in abet_csv_reader:
        if not colname_detected:
            if len(row) == 0:
                continue
            if row[0] == 'Animal ID':
                animal_descriptive_dictionary['Animal ID'] = str(row[2])
            if row[0] == 'Date/Time':
                date = str(row[1])
                date = date.replace(':', '-')
                date = date.replace('/', '-')
                animal_descriptive_dictionary['Date'] = date
            if row[0] in event_time_colname:
                colname_detected = True
                row[0] = 'Time'
                row[2] = 'Event_Time'
                animal_descriptive_dictionary['Time Variable'] = row[0]
                animal_descriptive_dictionary['Event Variable'] = row[2]
                abet_data_colname = [row[0], row[1], row[2], row[3], row[5], row[8]]
            else:
                continue
        else:
            abet_data_list.append([row[0], row[1], row[2], row[3], row[5], row[8]])

    abet_file.close()
    abet_np = np.array(abet_data_list)
    abet_pd = pd.DataFrame(data=abet_np, columns=abet_data_colname)
    return abet_pd, animal_descriptive_dictionary


def set_trial_structure(abet_data, session_dict, start_stages, end_stages):
    combined_stages = start_stages + end_stages
    abet_data_trial_stages = abet_data[abet_data.Item_Name.isin(combined_stages)]
    abet_data_trial_stages = abet_data_trial_stages.reset_index(drop=True)

    if abet_data_trial_stages.iloc[0, 3] not in start_stages:
        abet_data_trial_stages = abet_data_trial_stages.drop([0])

    abet_trial_times = abet_data_trial_stages.loc[:, session_dict['Time Variable']]
    abet_trial_times = abet_trial_times.reset_index(drop=True)
    abet_trial_start_times = abet_trial_times[::2]
    abet_trial_start_times = abet_trial_start_times.reset_index(drop=True)
    abet_trial_start_times = pd.to_numeric(abet_trial_start_times, errors='coerce')
    abet_trial_end_times = abet_trial_times[1::2]
    abet_trial_end_times = abet_trial_end_times.reset_index(drop=True)
    abet_trial_end_times = pd.to_numeric(abet_trial_end_times, errors='coerce')
    abet_trial_times = pd.concat([abet_trial_start_times, abet_trial_end_times], axis=1)
    abet_trial_times.columns = ['Start_Time', 'End_Time']
    abet_trial_times = abet_trial_times.reset_index(drop=True)
    return abet_trial_times

def search_event(dataset, start_event_id='1', start_event_group='', start_event_item_name='',
                          start_event_position=None,
                          filter_event=False, filter_list=None, extra_prior_time=0, extra_follow_time=0,
                          exclusion_list=None):
    if filter_list is None:
        filter_list = []

    def filter_event_data(event_data, abet_data, filter_type='', filter_name='', filter_group='', filter_arg='',
                          filter_before=1, filter_eval=''):
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
                    event_data[index] = np.nan
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

                # Equals
                if ',' in filter_arg:
                    filter_arg = filter_arg.split(',')

                if filter_eval == "inlist":
                    if filter_value not in filter_arg:
                        event_data[index] = np.nan
                if filter_eval == "notinlist":
                    if filter_value in filter_arg:
                        event_data[index] = np.nan
                if filter_eval == '=':
                    if float(filter_value) != float(filter_arg):
                        event_data[index] = np.nan
                if filter_eval == '!=':
                    if float(filter_value) == float(filter_arg):
                        event_data[index] = np.nan
                if filter_eval == '<':
                    if float(filter_value) >= float(filter_arg):
                        event_data[index] = np.nan
                if filter_eval == '<=':
                    if float(filter_value) > float(filter_arg):
                        event_data[index] = np.nan
                if filter_eval == '>':
                    if float(filter_value) <= float(filter_arg):
                        event_data[index] = np.nan
                if filter_eval == '>':
                    if float(filter_value) < float(filter_arg):
                        event_data[index] = np.nan

            event_data = event_data.dropna()
            event_data = event_data.reset_index(drop=True)
        return event_data

    touch_event_names = ['Touch Up Event', 'Touch Down Event', 'Whisker - Clear Image by Position']

    if start_event_id in touch_event_names:
        filtered_abet = dataset.loc[(dataset[self.event_name_col] == str(start_event_id)) & (
                self.abet_pandas['Group_ID'] == str(start_event_group)) &
                                             (self.abet_pandas['Item_Name'] == str(start_event_item_name)) & (
                                                     self.abet_pandas['Arg1_Value'] ==
                                                     str(start_event_position)), :]

    else:
        filtered_abet = self.abet_pandas.loc[(self.abet_pandas[self.event_name_col] == str(start_event_id)) & (
                self.abet_pandas['Group_ID'] == str(start_event_group)) &
                                             (self.abet_pandas['Item_Name'] == str(start_event_item_name)), :]

    self.abet_event_times = filtered_abet.loc[:, self.time_var_name]
    self.abet_event_times = self.abet_event_times.reset_index(drop=True)
    self.abet_event_times = pd.to_numeric(self.abet_event_times, errors='coerce')

    if filter_event:
        for fil in filter_list:
            self.abet_event_times = filter_event_data(self.abet_event_times, self.abet_pandas,
                                                      str(fil['Type']), str(fil['Name']),
                                                      str(fil['Group']), str(fil['Arg']),
                                                      str(fil['Prior']), str(fil['Eval']))

    abet_start_times = self.abet_event_times - extra_prior_time
    abet_end_times = self.abet_event_times + extra_follow_time
    self.abet_event_times = pd.concat([abet_start_times, abet_end_times], axis=1)
    self.abet_event_times.columns = ['Start_Time', 'End_Time']
    self.event_name = start_event_item_name
    self.extra_follow = extra_follow_time
    self.extra_prior = extra_prior_time
    return event_data

