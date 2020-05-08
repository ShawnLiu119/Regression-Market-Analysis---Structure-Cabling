import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

ispcu_reg = pd.read_csv("Regression_ISPCu.csv")
ispcu_reg = ispcu_reg.set_index("Year")
print(ispcu_reg)

corr = ispcu_reg.corr()

sns.set(style="white")
mask=np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

f,ax = plt.subplots(figsize=(11,9))
cmap = sns.diverging_palette(220,10,as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink":.5})
plt.show()
#using heatmap to tell directionally how variables corelated to each other
#because we have fewer columns and data points, the heatmap is not as ideal as expected

#data clearning
ispcu_reg["Real GDP"] = ispcu_reg["Real GDP"].str.replace("$","").astype("float")
ispcu_reg["GDP Growth Rate"] = ispcu_reg["GDP Growth Rate"].str.replace("%","").astype("float")
ispcu_reg["Unemployment Rate"] = ispcu_reg["Unemployment Rate"].str.replace("%","").astype("float")
ispcu_reg["Structured Cabling Market Sales"] = ispcu_reg["Structured Cabling Market Sales"].str.replace(",","").astype("float")

#using linear_regression model to train and test
target = ispcu_reg["Structured Cabling Market Sales"]
features = ispcu_reg.drop(["Structured Cabling Market Sales"], axis=1)

lr = LinearRegression(normalize=True)
est=sm.OLS(target, features)
est2 = est.fit()
print(est2.summary().tables[1])
#p value is 4th column, which indicate how strong the corelation between column and target column


