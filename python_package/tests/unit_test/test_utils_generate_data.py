import numpy as np
import pandas as pd

def test_duplicates_in_test_training(sample_input_data):
    '''Test the data leakage to detect if there are overlapped data between training dataset
    and test dataset
    '''

    x_train, y_train, x_test, y_test = sample_input_data 
    training_sample = pd.concat([pd.DataFrame(x_train), pd.DataFrame(y_train)], axis=1,
                            )
    training_sample.columns = ['x_train', 'y_train']
    testing_sample = pd.concat([pd.DataFrame(x_test), pd.DataFrame(y_test)], axis=1)
    testing_sample.columns = ['x_test', 'y_test']
    
    duplicates = pd.merge(training_sample, testing_sample, how='inner', 
                         left_on=['x_train', 'y_train'],
                         right_on = ['x_test', 'y_test'] 
                         )
    
    assert len(duplicates) < 2