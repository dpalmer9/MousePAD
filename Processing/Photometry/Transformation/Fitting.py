import numpy as np

def linear_lsr(fp_data):
    fit_func = np.polyfit(fp_data['Isobestic'], fp_data['Active'], 1)
    fit_lobf = np.multiply(fit_func[0], 'Isobestic') + fit_func[1]
    fp_data['Active'] = fit_lobf
    return fp_data


def delta_f(fp_data):
    fp_data['DeltaF'] = (fp_data['Active'] - fp_data['Isobestic']) / fp_data['Isobestic']
    return fp_data