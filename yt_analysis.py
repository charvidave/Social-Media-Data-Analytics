import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

youtube_data = pd.read_csv('video_result.csv')

#plt.figure()
#hist1, edges1 = np.histogram(youtube_data.viewCount)
#plt.bar(edges1[:-1],hist1, width=edges1[1:]-edges1[:-1])

#print(youtube_data.corr())

#plt.scatter(youtube_data.viewCount, youtube_data.likeCount)
#plt.show()

x=youtube_data.viewCount
y=youtube_data.likeCount
x=sm.add_constant(x)

lin_reg = sm.OLS(y,x).fit()
print(lin_reg.summary())