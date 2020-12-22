from pathlib import Path
import pandas as pd

folder="D:\My_Codes\Python\IEEE PRoject Prep\Stats-2018-19 season"
for file in Path(folder).glob('*.csv'):
	df = pd.read_csv(file)
	# df.columns = ['Unnamed: 0']
	df = df.drop( df.columns[0], axis = 1)
	# print(df)
	# df.rename(columns = {'OffRtg':'OFFRTG','DefRtg':'DEFRTG', 'NetRtg':'NETRTG', 'ASTRatio':'ASTRATIO', 'eFG%':'EFG%'}, inplace=True)
	# print(df)
	# df.loc[df.TEAM == 'LA Clippers', TEAM] = 'Los Angeles Clippers'
	# df.drop('Unnamed: 0', axis =1 )
	df.to_csv(file, index = False)
