import numpy as np
import pandas as pd

#Extraction
df=pd.read_csv("../Raw/owid-energy-data.csv")

#Cleaning
df=df[df['year']>2000]
df.dropna(subset=['iso_code','population'],inplace=True)

#Modelling
DimCountry=df[['iso_code','country']].drop_duplicates().reset_index(drop=True)
DimCountry.set_index('iso_code',inplace=True)

DimYear=df['year'].drop_duplicates().reset_index(drop=True)

columns=['iso_code','year','biofuel_consumption','biofuel_electricity','coal_consumption','coal_electricity','coal_production','fossil_fuel_consumption','fossil_electricity','gas_consumption','gas_electricity','gas_production','hydro_consumption','hydro_electricity','low_carbon_consumption','low_carbon_electricity','nuclear_consumption','nuclear_electricity','oil_consumption','oil_electricity','oil_production','other_renewable_consumption','other_renewable_electricity','renewables_consumption','renewables_electricity','solar_consumption','solar_electricity','wind_consumption','wind_electricity']
df1=df[columns]
df1.fillna(0,inplace=True)

melteddf1=df1.melt(id_vars=['iso_code','year'],var_name='EnergyVariable',value_name='Value')

melteddf1[['Type','Metric']]=melteddf1['EnergyVariable'].str.extract(r'(.+?)_(consumption|electricity|production)')

FactEnergy=melteddf1.pivot(index=['iso_code','year','Type'],columns='Metric',values='Value').reset_index()

DimType=FactEnergy['Type'].drop_duplicates().reset_index(drop=True)

columns=['iso_code','year','population','gdp','electricity_demand','electricity_generation','net_elec_imports','primary_energy_consumption','greenhouse_gas_emissions']
FactCountry=df[columns].reset_index(drop=True)

#Loading
FactCountry.to_csv("../DataWarehouse/FactCountry.csv")
FactEnergy.to_csv("../DataWarehouse/FactEnergy.csv")
DimCountry.to_csv("../DataWarehouse/DimCountry.csv")
DimYear.to_csv("../DataWarehouse/DimYear.csv")
DimType.to_csv("../DataWarehouse/DimType.csv")