import pandas as pd
from selenium import webdriver
import os
import time 


driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
# driver.implicitly_wait(30)
directory = 'D:\\My_Codes\\Python\\IEEE PRoject Prep\\Stats_'
url = 'https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2009-10&SeasonType=Regular%20Season&Month=1'
years = ['Season=2009-10', 'Season=2010-11', 'Season=2011-12', 'Season=2012-13', 'Season=2013-14', 'Season=2014-15', 'Season=2015-16', 'Season=2016-17', 'Season=2017-18']
seasonType = ['SeasonType=Regular%20Season', 'SeasonType=Playoffs']


for year in years:

	address = directory + year
	os.mkdir(address)
	parts = url.split('&')
	parts[2] = year
	parts[3] = seasonType[0]
	url = '&'.join(parts)

	for month in range(1,13):

		playoff = True
		parts = url.split('&')
		parts[3] = seasonType[0]
		parts[4] = 'Month=' + str(month)
		url = '&'.join(parts)
		try:
			print(url)
			driver.get(url)
			time.sleep(4)
			whichMonth = driver.find_element_by_class_name('stats-filter-pill__text').text
			print(whichMonth)
			html = driver.page_source
			df_list = pd.read_html(html)
			playoff = False
			df = df_list[0] 
			df = df.dropna(axis = 1, how = 'any')
			df.rename(columns = {'OffRtg':'OFFRTG','DefRtg':'DEFRTG', 'NetRtg':'NETRTG', 'ASTRatio':'ASTRATIO', 'eFG%':'EFG%'}, inplace=True)
			df.drop('Unnamed: 0', axis = 1, inplace = True)
			df.loc[df['TEAM'] == 'LA Clippers', 'TEAM'] = 'Los Angeles Clippers'
			df.to_csv(address + '\\' + whichMonth + '.csv', index = False)
		except:
			print('exception!'+ 'regular')

		if playoff == True:
			try:
				new = url.split('&')
				new[3] = seasonType[1]
				url = '&'.join(new)
				print(url)
				driver.get(url)
				time.sleep(4)
				whichMonth = driver.find_element_by_class_name('stats-filter-pill__text').text
				print(whichMonth)
				html = driver.page_source
				df_list = pd.read_html(html)
				df = df_list[0] 
				df = df.dropna(axis = 1, how = 'any')
				df.rename(columns = {'OffRtg':'OFFRTG','DefRtg':'DEFRTG', 'NetRtg':'NETRTG', 'ASTRatio':'ASTRATIO', 'eFG%':'EFG%'}, inplace=True)
				df.drop('Unnamed: 0', axis = 1, inplace = True)
				df.loc[df['TEAM'] == 'LA Clippers', 'TEAM'] = 'Los Angeles Clippers'
				df.to_csv(address + '\\' + whichMonth + '.csv', index = False)
			except:
				print('exception!Playoff')
				continue
