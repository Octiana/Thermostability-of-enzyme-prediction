
# Base libraries
import numpy as np
import pandas as pd
import random

## Novozymes Database
test= "./novozymes-enzyme-stability-prediction/test.csv"
train = "./novozymes-enzyme-stability-prediction/train.csv"

sampleSubmission = "./novozymes-enzyme-stability-prediction/sample_submission.csv"
trainUpdates = "./novozymes-enzyme-stability-prediction/train_updates_20220929.csv"

pdbPath = "./novozymes-enzyme-stability-prediction/wildtype_structure_prediction_af2.pdb"

data_test = pd.read_csv(test)
data_test.head()
print(data_test)
