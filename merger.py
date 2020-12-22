import pandas as pd
import numpy as np
import os

dirstat = input("Enter Stats")
dirres = input("Enter results")

stat = sorted(os.listdir(dirstat))
res = sorted(os.listdir(dirres))

# print(stat)
# print(res)

dflist = list()

# Adding a new binary columns for Team 1 Win or Loss
for i in range(len(res)):
	results = res[i]
	stats = stat[i]
	# print(os.path.join(results, dirres)+"\\"+ res[i])
	results = pd.read_csv(os.path.join(results, dirres)+"\\"+ res[i]);
	stats = pd.read_csv(os.path.join(stats, dirstat)+"\\"+ stat[i]);
	conditions = [
	results['Team1Score'] > results['Team2Score'],
	results['Team1Score'] < results['Team2Score']
	]

	choices=[1,0]

	results['Team1Win'] = np.select(conditions, choices, 1)

	# Mergings the results and stats datasets, adding a prefix depending on which teams stats are being used
	df = results.merge(stats.add_prefix('Team1'), how='left', left_on=['Team1'], 
	       right_on=['Team1TEAM']).drop(['Team1TEAM'],
	                                    axis=1).merge(stats.add_prefix('Team2'), 
	                                                                how='left', left_on=['Team2'], 
	                                                                right_on=['Team2TEAM']).drop(['Team2TEAM'],axis=1)
	df = df.drop_duplicates(keep = False)
	dflist.append(df)
	# name = "data" + str(i) + ".csv"
	# df.to_csv(name, index = False, header=True)   

ans = pd.concat(dflist)
drp = ['Team1Score', 'Team1', 'Team2', 'Team2Score']
ans.drop(drp, axis = 1, inplace=True)
ans = ans.drop_duplicates(keep = False)
ans.dropna(inplace = True)
ans.to_csv('data-2017-18.csv', index = False, encoding='utf-8-sig')
