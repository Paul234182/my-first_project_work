import pandas as pd
import numpy as np
food_consumption= pd.read_csv('food_consumption.csv')
print(food_consumption)
food_consumption.describe()
print(food_consumption.describe())
print(food_consumption.head())

np.mean(food_consumption['consumption'] > 30)
print(np.mean(food_consumption['consumption'] > 30))

np.median(food_consumption['co2_emission'])
print(np.median(food_consumption['co2_emission']))

food_consumption.loc[food_consumption['co2_emission'] > 35.22]['consumption']
print(food_consumption.loc[food_consumption['co2_emission'] > 35.22]['consumption'])
food_consumption.dtypes
print(food_consumption.dtypes)

MASK1= food_consumption['consumption']>= 3.24
MASK2= food_consumption['country']== 'USA'
food_consumption2= food_consumption[MASK1 & MASK2].sort_values(by= 'consumption', ascending= True)
print(food_consumption2)
food_consumption.groupby('country')['co2_emission'].mean()
print(food_consumption.groupby('country')['co2_emission'].mean())
# Calculate total co2_emission per country: 

food_consumption.groupby('country')['co2_emission'].sum().sort_values( ascending= False)
print(food_consumption.groupby('country')['co2_emission'].sum().sort_values( ascending= False))
# Calculate mean and median consumption in Belgium
be_consumption= np.mean(food_consumption['country']== 'Belgium')
print(be_consumption)
be_consumption= np.median(food_consumption['country']== 'Belgium')
print(be_consumption)

be_consumption= food_consumption.groupby(food_consumption ['country']== 'Belgium')['consumption'].mean()
print(be_consumption)

def consumption():
  results=  food_consumption['co2_emission'].strip().lower()
  return results
print(results)


