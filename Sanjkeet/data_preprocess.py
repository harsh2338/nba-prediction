import pandas as pd

file = 'D:\My_Codes\Python\IEEE PRoject Prep\Data_2010-2019\DATA(2010-2019).csv'
df = pd.read_csv(file)
df.drop(['Team1GP', 'Team1W', 'Team1L', 'Team1MIN','Team2GP', 'Team2W', 'Team2L', 'Team2MIN'], axis = 1, inplace = True)
df.to_csv('D:\My_Codes\Python\IEEE PRoject Prep\Data_2010-2019\DATA_final.csv', index = False)