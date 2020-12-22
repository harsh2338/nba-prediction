from pathlib import Path
import pandas as pd
import os, sys

folder=input("Enter Folder")
count = 0
# for file in Path(folder).glob('*.*'):
# 	df = pd.read_csv(str(file))
# 	count += 1
# 	l = [0,1,2,7,8,9,10]
# 	df = df.drop(df.columns[l], axis = 1, inplace = True)
# 	type(df)
# 	# df.columns = ['Team1', 'Team1Score', 'Team2', 'Team2Score']
# 	# df.to_csv(file, index = False)
# # print(count)

dirs = os.listdir(folder)
for file in dirs:
    if file == '*.csv':
    	df = pdf.read_csv(file)
    	l = [0,1,2,7,8,9,10]
    	df = df.drop(df.columns[l], axis = 1, inplace = True)
    	df.columns = ['Team1', 'Team1Score', 'Team2', 'Team2Score']
    	df.to_csv(file, index = False)