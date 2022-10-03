# Imports
import numpy as np
import pandas as pd


# Functions

def remove_pre_observations(fp_data):
    fp_data = fp_data[fp_data['Time'] >= 0]
    return fp_data
