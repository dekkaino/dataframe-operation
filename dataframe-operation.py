import pandas as pd
import numpy as np

columnNames = ['ほげ','ふが','95%','ぽにょ']
indexNumber = 0

df_list = {}

numberlist = np.arange(4)
#print(numberlist)

df1 = pd.DataFrame([numberlist], columns=['col_0', 'col_1', 'col_2', 'col_3'])

for columnName in columnNames:
  df_list[columnName] = df1 + indexNumber
  indexNumber = indexNumber +1

print(df_list)

print('--- merge df---')

for columnName in columnNames:
  if 'merge' in df_list:
    df_list['merge'] = df_list['merge'].append(df_list[columnName])
  else:
    df_list['merge'] = df_list[columnName]

print(df_list['merge'])
