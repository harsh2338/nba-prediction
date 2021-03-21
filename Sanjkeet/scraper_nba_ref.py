import pandas as pd
from bs4 import BeautifulSoup 
import os
import urllib

url = 'https://www.basketball-reference.com/leagues/'
directory = 'D:\\My_Codes\\Python\\IEEE PRoject Prep\\Results_'
end = ['NBA_2010_games','NBA_2011_games', 'NBA_2012_games', 'NBA_2013_games' , 'NBA_2014_games', 'NBA_2015_games', 'NBA_2016_games', 'NBA_2017_games', 'NBA_2018_games']
for i in range(9):
	address = directory + end[i]
	os.mkdir(address)
	url_ = url + end[i]
	url_ += '.html'
	print(url_)
	url_ = urllib.request.urlopen(url_).read()
	soup = BeautifulSoup(url_, 'html.parser')
	div = soup.find('div', attrs = {'class' : 'filter'})
	links = div.find_all('div')
	for link in links:
		link = link.find('a')
		df_list = pd.read_html('https://www.basketball-reference.com' + link['href'])
		df = df_list[0]
		l = [0,1,6,7,8,9]
		df.drop(df.columns[l], axis = 1, inplace = True)
		df.columns = ['Team1', 'Team1Score', 'Team2', 'Team2Score']
		df.to_csv(address + '\\' + link.text + '.csv', index = False)