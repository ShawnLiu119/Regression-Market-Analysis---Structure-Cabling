# Regression-Market-Analysis---Structure-Cabling
Analyze Structured Cabling Copper Market vs key macroeconomic indicators

The project is trying to figure out and analyze the corelation between structured cabling market and key macro economic indicators. For those who is not familiar with structured cabling, here is a good introduction to read https://en.wikipedia.org/wiki/Structured_cabling

The data is collected from multiple websites and sources

Indicators | Source | Description | Unit|
--- | --- | --- | --- |
Stuctured Cabling Market Sales | BSRIA Research | market size of stuctured cabling for copper | $ Million | 
US Commercial Construction | US Concensus Bureau | US construction spending | $ Billion |
Construction Spending (Private + Public) | Statista.com | *** | $ Billions |
Real GDP | thebalance.com | *** | $ Trillions | 
GDP Growth Rate | thebalance.com | *** | % percentage | 
Copper Commodity Price | fred.stlouisfed.org | global copper price | Metric Tons |

Conclusion：
Based on p_value output, top 3 indicators of strongest corelations are Copper Commodity Price, Unemployment, Construction Spending 
============================================================================================================
                                               coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------------------------
Value of U.S. commercial construction        1.3474      2.024      0.666      0.518      -3.063       5.758
Construction Spending (Private + Public)     0.7003      0.284      2.462      0.030       0.080       1.320
Real GDP                                     6.2764     15.176      0.414      0.686     -26.790      39.342
GDP Growth Rate                             14.2002      8.859      1.603      0.135      -5.101      33.501
Unemployment Rate                           30.5962      7.970      3.839      0.002      13.232      47.960
Copper Commodity Price                       0.0442      0.006      6.911      0.000       0.030       0.058
