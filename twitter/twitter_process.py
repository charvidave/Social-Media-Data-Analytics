import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

twitter_data = pd.read_csv('result1.csv')


x=twitter_data.followers
y=twitter_data.retwc
x=sm.add_constant(x)

lin_reg = sm.OLS(y,x).fit()
print(lin_reg.summary())
