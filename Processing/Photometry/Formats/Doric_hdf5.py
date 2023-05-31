# Import
import pandas as pd
import numpy as np
import h5py


# Functions
def read_data(file_path):
    doric_data = pd.read_csv(file_path, header=1)
    return doric_data


def extract_data(doric_data, iso, act, ttl, mode):
    if mode == 'lockedin':
        iso_col = iso.split(',')
        iso_in = str(iso_col[0])
        iso_in = iso_in.rjust(2, '0')
        iso_in = 'AIN' + iso_in
        iso_out = str(iso_col[1])
        iso_out = iso_out.rjust(2, '0')
        iso_out = 'AOUT' + iso_out
        act_col = act.split(',')
        act_in = str(act_col[0])
        act_in = act_in.rjust(2, '0')
        act_in = 'AIN' + act_in
        act_out = str(act_col[1])
        act_out = act_out.rjust(2, '0')
        act_out = 'AOUT' + act_out
        ttl_in = str(ttl)
        ttl_in = ttl_in.rjust(2, '0')
        ttl_in = 'AIN' + ttl_in

        dataset_keys = doric_data.keys()
        for key in dataset_keys:
            if iso_in in key:
                if iso_out in key:
                    key_name = iso_in + 'x' + iso_out + '-LockIn'
                    iso_dataset = doric_data[key]
                    lock_time = iso_dataset['Time']
                    lock_time = np.array(lock_time)
                    iso_data = iso_dataset['Values']
                    iso_data = np.array(iso_data)

            if act_in in key:
                if act_out in key:
                    key_name = act_in + 'x' + act_out + '-LockIn'
                    act_dataset = doric_data[key]
                    act_data = act_dataset['Values']
                    act_data = np.array(act_data)

        ttl_keys = doric_data['AnalogIn'].keys()

        for key in ttl_keys:
            if ttl_in in key:
                ttl_time = doric_data['AnalogIn']['Time']
                ttl_time = np.array(ttl_time)
                ttl_data = doric_data['AnalogIn'][key]
                ttl_data = np.array(ttl_data)

        signal_data = pd.DataFrame({'Time': lock_time, 'Control': iso_data, 'Active': act_data})
        signal_data = signal_data.astype('float')
        ttl_data = pd.DataFrame({'Time': ttl_time, 'TTL': ttl_data})
        ttl_data = ttl_data.astype('float')