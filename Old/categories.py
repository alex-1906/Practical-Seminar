import pandas as pd
import numpy as np

data = pd.read_csv('../movies.csv')
print(data.columns)

data_genres = pd.pivot_table(data,index=data['title'],columns=data['genres'])
print(data.loc[0])
#print(data['genres'].values)

data2 = pd.read_csv('movies_metadata.csv',low_memory=False)
print(data2['genres'])