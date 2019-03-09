#####
# to install any prog that might need..
# then run in TERMINAL --- see below  PROBLEMS | OUTPUT | DEBUG CONSOLE |  ...TERMINAL... 
# python -m pip install --upgrade program_needed_as_an_example

## as an example try below to upgrade/install numpy...
# python -m pip install --upgrade numpy
## if there already it'll say that it is uptodate

# and also good to import numpy as well as it has scipy and all that...
import pandas as pd
import numpy as np

#### FOR TO GRAB DATA FROM EXCEL NEED TO INSTALL xlrd
#### USE COMMAND BELOW
## python -m pip install --upgrade xlrd
## 
	
##from sqlalchemy import create_engine
##engine = create_engine('sqlite:///:memory:')
    
##sql_dataframe   = pd.read_sql_table('my_table', engine, columns=['ColA', 'ColB'])
## NEED TO ADD PATH C:\Users\Gerry\Source\Repos\PythonApplication1\PythonApplication1 BEFORE FILE NAME sample_test_dataset.xlsx

## DIRECTLY FROM PAGE Course > Data And Features > Manipulating Data > Loading Data 
## IN edX.org
## Microsoft: DAT210x 
## Programming with Python for Data Science
## This is the line to use....
#xls_dataframe   = pd.read_excel('C:\Users\Gerry\Source\Repos\PythonApplication1\PythonApplication1\sample_test_dataset.xlsx', 'Sheet1', na_values=['NA', '?'])
# SHOW ERROR
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

# NEED TO DOUBLE THE BACK SLASHES \ TO \\
## PATH BELOW HAS TO BE WHERE THE DATASET IS STORED sample_test_dataset.xlsx
## FOUND THIS ONE ONLINE WITH SEARCH
xls_dataframe   = pd.read_excel('C:\\Users\\Gerry\\Source\\Repos\\PythonApplication1\\PythonApplication1\\sample_test_dataset.xlsx', 'sample_test_dataset', na_values=['NA', '?'])


print(xls_dataframe.dtypes) # just show type of data for each column either a number or an object (yet undefined)
  
###json_dataframe  = pd.read_json('my_dataset.json', orient='columns')
##csv_dataframe   = pd.read_csv('my_dataset.csv', sep=',')
##table_dataframe = pd.read_html('http://page.com/with/table.html')[0]