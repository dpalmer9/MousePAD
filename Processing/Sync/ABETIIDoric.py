# Import

# Functions

def data_ttl_sync(behaviour_object, neural_object):
    photo_data = neural_object.condensed_data.iloc[:, [0,3]]
    behav_data =