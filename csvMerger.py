import os
import glob
import pandas as pd
os.chdir("D:\My_Codes\Python\IEEE PRoject Prep\Data_2010-2019")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "data-2010-19.csv", index=False, encoding='utf-8-sig')