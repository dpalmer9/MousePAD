# Import
from scipy import signal


def butterworth(time_data, data_iso, data_act, order, filter_freq, filt_type='lowpass', analog=False):
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    butter_filter = signal.butter(N=order, Wn=filter_freq, btype=filt_type, analog=analog,
                                  output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(butter_filter, data_iso)
    fil_act = signal.sosfilt(butter_filter, data_act)
    return fil_iso, fil_act


def chebychev_i(time_data, data_iso, data_act, order, ripple, filter_freq, filt_type='lowpass', analog=False):
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    chebyi_filter = signal.cheby1(N=order, rp=ripple, Wn=filter_freq, btype=filt_type, analog=analog,
                                  output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(chebyi_filter, data_iso)
    fil_act = signal.sosfilt(chebyi_filter, data_act)
    return fil_iso, fil_act


def chebychev_ii(time_data, data_iso, data_act, order, attenuation, filter_freq, filt_type='lowpass', analog=False):
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    chebyii_filter = signal.cheby2(N=order, rs=attenuation, Wn=filter_freq, btype=filt_type, analog=analog,
                                   output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(chebyii_filter, data_iso)
    fil_act = signal.sosfilt(chebyii_filter, data_act)
    return fil_iso, fil_act


def bessel(time_data, data_iso, data_act, order, filter_freq, filt_type='lowpass', analog=False):
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    bessel_filter = signal.bessel(N=order, Wn=filter_freq, btype=filt_type, analog=analog,
                                  output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(bessel_filter, data_iso)
    fil_act = signal.sosfilt(bessel_filter, data_act)
    return fil_iso, fil_act


def elliptic(time_data, data_iso, data_act, order, ripple, attenuation, filter_freq, filt_type='lowpass', analog=False):
    sample_freq = len(time_data) / (time_data[(len(time_data) - 1)] - time_data[0])
    ellip_filter = signal.ellip(N=order, rp=ripple, rs=attenuation, Wn=filter_freq, btype=filt_type, analog=analog,
                                output='sos', fs=sample_freq)
    fil_iso = signal.sosfilt(ellip_filter, data_iso)
    fil_act = signal.sosfilt(ellip_filter, data_act)
    return fil_iso, fil_act
