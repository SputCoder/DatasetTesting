## DIRECTLY FROM PAGE Course > Data And Features > Manipulating Data > Loading Data 
## IN edX.org
## Microsoft: DAT210x 
## Programming with Python for Data Science

#### TAKES ABOUT 10 SEC TO RUN IF A LOT OF DATA....

# and also good to import numpy as well as it has scipy and all that...
import pandas as pd
import numpy as np

## IF DON'T HAVE pandas ALREADY INSTALLED, I THINK CAN USE FOLLOWING COMMAND IN THE TERMINAL (BOTTOM HALF OF EDITOR)
## python -m pip install --upgrade pandas
## SIMILARLY FOR numby
## python -m pip install --upgrade numpy # numpy not numby??  me thinks :)

#### FOR TO GRAB DATA FROM EXCEL NEED TO INSTALL xlrd
#### USE COMMAND BELOW
## python -m pip install --upgrade xlrd
## 

# NEED TO DOUBLE THE BACK SLASHES \ TO \\
## PATH BELOW HAS TO BE WHERE THE DATASET IS STORED sample_test_dataset.xlsx
## FOUND THIS ONE ONLINE WITH SEARCH
## WAS A TEXT FILE BUT IMPORTING INTO EXCEL... COS EXCEL IS GOOD :)
xls_dataframe   = pd.read_excel('C:\\Users\\Gerry\\Source\\Repos\\PythonApplication1\\PythonApplication1\\sample_test_dataset.xlsx', 'sample_test_dataset', na_values=['NA', '?'])

print(xls_dataframe.dtypes) # just show type of data for each column either a number or an object (yet undefined)



