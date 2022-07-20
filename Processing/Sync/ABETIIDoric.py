# Import

# Functions

def data_ttl_sync(behaviour_object, neural_object):
    photo_data = neural_object.condensed_data.iloc[:, [0,3]]
    behav_data = behaviour_object.main_dataset

    photo_cols = photo_data.columns
    photo_ttl = photo_data.loc[photo_data[[photo_cols[3]]] > 1.00, ]
