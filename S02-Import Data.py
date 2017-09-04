import cauldron as cd
import pandas as pd

#----------------------------------------------------------------------
### Import csv files and share it with other steps. 
#----------------------------------------------------------------------

#import csv data 
epc = pd.read_csv('EnterprisesPerCountry.csv')
mg = pd.read_csv('LatinAmericaInternetUsersGrowth.csv')

#make data available for other steps
cd.shared.epc = epc 
cd.shared.mg = mg