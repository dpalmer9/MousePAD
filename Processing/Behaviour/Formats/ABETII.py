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


def abet_set_trial_structure(abet_data, session_dict, start_stages, end_stages):
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

