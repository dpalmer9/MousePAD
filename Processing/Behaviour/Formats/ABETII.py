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
                abet_data_colname = [row[0], row[1], row[2], row[3], row[5], row[8]]
            else:
                continue
        else:
            abet_data_list.append([row[0], row[1], row[2], row[3], row[5], row[8]])

    abet_file.close()
    abet_np = np.array(abet_data_list)
    abet_pd = pd.DataFrame(data=abet_np, columns=abet_data_colname)
    return abet_pd, animal_descriptive_dictionary

