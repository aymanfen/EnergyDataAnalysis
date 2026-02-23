import numpy as np
import pandas as pd

#Extract
df=pd.read_csv("../DataWarehouse/DimType.csv",index_col=0)

#Transform - Enrich
energy_source_to_type = {
    'biofuel': ('Renewable', 'Renewable'),
    'coal': ('Non-Renewable', 'Fossil Fuel'),
    'fossil': ('Non-Renewable', 'Fossil Fuel'),
    'fossil_fuel': ('Non-Renewable', 'Fossil Fuel'),
    'gas': ('Non-Renewable', 'Fossil Fuel'),
    'hydro': ('Renewable', 'Hydroelectric'),
    'low_carbon': ('Non-Renewable', 'Low-Carbon'),
    'nuclear': ('Non-Renewable', 'Nuclear'),
    'oil': ('Non-Renewable', 'Fossil Fuel'),
    'other_renewable': ('Renewable', 'Other Renewable'),
    'renewables': ('Renewable', 'Renewable Energy'),
    'solar': ('Renewable', 'Solar'),
    'wind': ('Renewable', 'Wind')
}


df[['AltCategory', 'Category']] = df['Type'].apply(
     lambda x: pd.Series(energy_source_to_type.get(x, (None, None))))

#Load
df.to_csv("../DataWarehouse/DimType.csv")

