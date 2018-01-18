import pandas as pd

df = pd.read_csv("Workbook2.csv")
print(df.columns.values)

list = ['Name', 'DOB']
print(len(set(df.columns.values).intersection(list)))