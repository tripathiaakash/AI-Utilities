import matplotlib.pyplot as plt
import seaborn as sns
import math

def boxplots(df):
    n_features = len(df.columns.values)
    
    ncol = 2
    nrow = math.ceil(n_features/ncol)
    figsize = (20, nrow*5)
    
    f, axes = plt.subplots(nrow, ncol, figsize = figsize)
    i = 0
    j = 0
    n = 0
    for colname in df.columns.values:
        sns.boxplot(x = df[colname], color = "blue", ax = axes[i, j])
        n+=1
        i = int(n/2)
        j = int((j+1)%2)
