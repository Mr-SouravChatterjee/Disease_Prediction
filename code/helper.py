import pandas as pd
import numpy as np


def prepare_symptoms_array(symptoms):
    symptoms_array = np.zeros((1,133))
    df = pd.read_csv('data/clean_dataset.tsv', sep='\t')
    
    for symptom in symptoms:
        symptom_idx = df.columns.get_loc(symptom)
        symptoms_array[0, symptom_idx] = 1

    return symptoms_array