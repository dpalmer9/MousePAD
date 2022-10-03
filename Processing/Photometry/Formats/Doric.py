# Import
import pandas as pd


# Functions
def read_data(file_path):
    doric_data = pd.read_csv(file_path, header=1)
    return doric_data


def extract_data(doric_data, iso, act, ttl):
    iso_index = False
    act_index = False
    ttl_index = False
    if isinstance(iso, int):
        iso_index = True
    if isinstance(act, int):
        act_index = True
    if isinstance(ttl_index, int):
        ttl_index = True

    time_data = doric_data.iloc[:, 0]

    if iso_index:
        iso_data = doric_data.iloc[:, iso]
    else:
        iso_data = doric_data[iso]

    if act_index:
        act_data = doric_data.iloc[:, act]
    else:
        act_data = doric_data[act]

    if ttl_index:
        ttl_data = doric_data.iloc[:, ttl]
    else:
        ttl_data = doric_data[ttl]

    session_data = pd.concat([time_data, iso_data, act_data, ttl_data])
    session_data.columns = ['Time', 'Isobestic', 'Active', 'TTL']
    return session_data
