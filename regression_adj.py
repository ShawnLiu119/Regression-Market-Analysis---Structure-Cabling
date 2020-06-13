# Regression model of ISPCU market

import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('ISPCU_data (AR)_cons.csv', sep=',', index_col='Year')    
df['Unemployment Rate'] = np.log(df['Unemployment Rate'])
df['Real GDP'] = np.log(df['Real GDP'])

train = df[2003:2019]
factors = train.drop(['Structured Cabling Market Sales (current period)'],axis=1)
target = train[['Structured Cabling Market Sales (current period)']]

print(train)

est = sm.OLS(target, factors).fit()
print(est.summary().tables[1])
print('adjusted r-squared:', est.rsquared_adj)

def model(scenario):
    train = df[2003:2019]
    feature = train[scenario]
    target = train[['Structured Cabling Market Sales (current period)']]

    test = df.loc[2020:2021.75, scenario]
    
    lr = LinearRegression()
    lr.fit(feature, target)
    prediction = lr.predict(test)

    return target, prediction

scenario_1 = ['Construction Spending (Private + Public)', 'Real GDP', 'Unemployment Rate', 'Copper_Price_ChiEx']
scenario_2 = ['Construction Spending (Private + Public)', 'GDP Growth Rate', 'Unemployment Rate', 'Copper_Price_ChiEx']
scenario_3 = ['Construction Spending (Private + Public)', 'Worst_GDP', 'Unemployment Rate', 'Copper_Price_ChiEx']
scenario_4 = ['Construction Spending (Private + Public)', 'Real GDP', 'Unemployment Rate', 'Copper_Price_gov']
scenario_5 = ['Construction Spending (Private + Public)', 'GDP Growth Rate', 'Unemployment Rate', 'Copper_Price_gov']
scenario_6 = ['Construction Spending (Private + Public)', 'Worst_GDP', 'Unemployment Rate', 'Copper_Price_gov']
scenario_list = [scenario_1, scenario_2, scenario_3, scenario_4, scenario_5, scenario_6] 

color = ["black", "orange", "red", "green", "blue", "purple"]

   
plt.figure(figsize=[12,6])
historical_values = df['Structured Cabling Market Sales (current period)'][2003:2019] # model(scenario_list[i])[0]
plt.plot(historical_values, data=historical_values, label='Historical Data')

for i in range(len(scenario_list)):
    prediction = model(scenario_list[i])[1]
       
    # Set last point in historical data as first point in prediction
    t = max(historical_values.index)
    c = 'Structured Cabling Market Sales (current period)'
    v = historical_values[2019]
        
    prediction = prediction[::-1]
    prediction_c = pd.DataFrame(prediction)
    production_c = prediction_c.set_index(pd.Index([2021.75, 2021.5, 2021.25, 2021, 2020.75, 2020.5, 2020.25, 2020]), inplace=True)
    prediction_c.loc[t, 0] = v
    prediction_c.rename(columns={0: 'Structured Cabling Market Sales (current period)'})
        
    # Plot figure
    
    label = "Scenario" + str(i+1)
    plt.plot(prediction_c[::-1], label=label, color=color[i])

plt.legend()
plt.ylabel("Structured Cabling Market Sales")
plt.xlabel("Year")
plt.xlim(2002,2022)
plt.xticks(range(2002,2022,1))
plt.ylim([800,2200])
plt.yticks(range(800,2200,100))
plt.show()


plt.figure(figsize=[8,6])
for i in range(len(scenario_list)):
    prediction_1 = model(scenario_list[i])[1]
          
    prediction_c = pd.DataFrame(prediction_1, columns = ['Structured Cabling Market Sales (current period)'])
    prediction_c.set_index(pd.Index(["Q1-20", "Q2-20", "Q3-20", "Q4-20", "Q1-21", "Q2-21", "Q3-21", "Q4-21"]), inplace=True)   

    # Plot figure
    
    label = "Scenario" + str(i+1)
    plt.plot('Structured Cabling Market Sales (current period)', data = prediction_c, label=label, color=color[i])

plt.legend()
plt.xticks(np.arange(8),("Q1-20", "Q2-20", "Q3-20", "Q4-20", "Q1-21", "Q2-21", "Q3-21", "Q4-21"))
plt.ylim([800,2200])
plt.yticks(range(800,2200,100))
plt.show()
    

# End of file
