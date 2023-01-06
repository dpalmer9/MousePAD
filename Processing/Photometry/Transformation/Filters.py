# Import
from scipy import signal

# Butterworth Filter


def butterworth(fp_data, order, filter_freq, filt_type='lowpass', analog=False):
    time_data = fp_data['Time']
    data_iso = fp_data['Isobestic']
    data_act = fp_data['Active']
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    butter_filter = signal.butter(N=order, Wn=filter_freq, btype=filt_type, analog=analog,
                                  output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(butter_filter, data_iso)
    fil_act = signal.sosfilt(butter_filter, data_act)
    fp_data['Isobestic'] = fil_iso
    fp_data['Active'] = fil_act
    return fp_data

# Chebychev Type I Filter


def chebychev_i(fp_data, order, ripple, filter_freq, filt_type='lowpass', analog=False):
    time_data = fp_data['Time']
    data_iso = fp_data['Isobestic']
    data_act = fp_data['Active']
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    chebyi_filter = signal.cheby1(N=order, rp=ripple, Wn=filter_freq, btype=filt_type, analog=analog,
                                  output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(chebyi_filter, data_iso)
    fil_act = signal.sosfilt(chebyi_filter, data_act)
    fp_data['Isobestic'] = fil_iso
    fp_data['Active'] = fil_act
    return fp_data

# Chebychev Type II Filter


def chebychev_ii(fp_data, order, attenuation, filter_freq, filt_type='lowpass', analog=False):
    time_data = fp_data['Time']
    data_iso = fp_data['Isobestic']
    data_act = fp_data['Active']
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    chebyii_filter = signal.cheby2(N=order, rs=attenuation, Wn=filter_freq, btype=filt_type, analog=analog,
                                   output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(chebyii_filter, data_iso)
    fil_act = signal.sosfilt(chebyii_filter, data_act)
    fp_data['Isobestic'] = fil_iso
    fp_data['Active'] = fil_act
    return fp_data

# Bessel Filter


def bessel(fp_data, order, filter_freq, filt_type='lowpass', analog=False):
    time_data = fp_data['Time']
    data_iso = fp_data['Isobestic']
    data_act = fp_data['Active']
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    bessel_filter = signal.bessel(N=order, Wn=filter_freq, btype=filt_type, analog=analog,
                                  output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(bessel_filter, data_iso)
    fil_act = signal.sosfilt(bessel_filter, data_act)
    fp_data['Isobestic'] = fil_iso
    fp_data['Active'] = fil_act
    return fp_data

# Elliptic Filter


def elliptic(fp_data, order, ripple, attenuation, filter_freq, filt_type='lowpass', analog=False):
    time_data = fp_data['Time']
    data_iso = fp_data['Isobestic']
    data_act = fp_data['Active']
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    ellip_filter = signal.ellip(N=order, rp=ripple, rs=attenuation, Wn=filter_freq, btype=filt_type, analog=analog,
                                output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(ellip_filter, data_iso)
    fil_act = signal.sosfilt(ellip_filter, data_act)
    fp_data['Isobestic'] = fil_iso
    fp_data['Active'] = fil_act
    return fp_data

# Savitsky-Golay Filter


def savitsky_golay(fp_data, polyorder):
    time_data = fp_data['Time']
    data_iso = fp_data['Isobestic']
    data_act = fp_data['Active']
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    window_length = int(round(sample_freq) / 10)

    fil_iso = signal.savgol_filter(data_iso, window_length, polyorder)
    fil_act = signal.savgol_filter(data_act, window_length, polyorder)

    fp_data['Isobestic'] = fil_iso
    fp_data['Active'] = fil_act
    return fp_data
