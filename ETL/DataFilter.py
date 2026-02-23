import numpy as np
import pandas as pd

SelectedCountries=['USA','CHN','JPN','DEU','IND','GBR','FRA','ITA','CAN','BRA','RUS','KOR','AUS','ESP','MEX','IDN','NLD','SAU','TUR','CHE','TWN','POL','SWE','BEL','THA']

#Fact Energy
df=pd.read_csv("../DataWarehouse/FactEnergy.csv",index_col=0)

df=df[df['iso_code'].isin(SelectedCountries)]
df.fillna(0,inplace=True)

df.to_csv("../DataWarehouse/FactEnergy.csv")

#FactCountry
df1=pd.read_csv("../DataWarehouse/FactCountry.csv",index_col=0)

df1=df1[df1['iso_code'].isin(SelectedCountries)]

df1.to_csv("../DataWarehouse/FactCountry.csv")