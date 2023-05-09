# Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


# Loading datasets
in_time = pd.read_csv('soucre/in_time.csv')
manager_survey_data = pd.read_csv('soucre/manager_survey_data.csv')
employee_survey_data = pd.read_csv('soucre/employee_survey_data.csv')
out_time = pd.read_csv('soucre/out_time.csv')
general_data = pd.read_csv('soucre/general_data.csv')
data_dictionary= pd.read_excel('soucre/data_dictionary.xlsx', engine='openpyxl')
# checking dimensions of each set
print(in_time.shape)
print(manager_survey_data.shape)
print(employee_survey_data.shape)
print(data_dictionary.shape)
print(out_time.shape)
print(general_data.shape)

# Previewing data
print(in_time.head())
print(manager_survey_data.head())
print(employee_survey_data.head())
print(data_dictionary.head())
print(out_time.head())
print(general_data.head())



# append in_time to out_time
in_time = pd.concat([in_time, out_time])

in_time=in_time.replace(np.nan,0)
in_time.iloc[:, 1:] = in_time.iloc[:, 1:].apply(pd.to_datetime, errors='coerce')
in_time=in_time.replace(np.nan,0)
in_time.iloc[:, 1:] = in_time.iloc[:, 1:].apply(pd.to_datetime, errors='coerce')


in_time=in_time.diff(periods=4410)
in_time=in_time.iloc[4410:]


in_time['Unnamed: 0']=in_time['Unnamed: 0'].replace(0,np.NaN)
in_time=in_time.replace('0 days 00:00:00',np.NaN)



time = in_time.copy()


time['Average time']=time.mean(axis=1)
time['Total days'] = time.iloc[:, 1:261].count(axis=1)
time['Total hours']=time.iloc[:, 1:261].sum(axis=1)

time['Unnamed: 0'] = range(1, len(time)+1)
