#Takes a pandas dataframe and a list of column names which are to be log transformed
# Gives out log(x+1) tranformed columns along with unmutilated columns

import numpy as np
def log_transform(df, colname_list):
    df1 = df.copy()
    for colname in colname_list:
        df1[colname] = np.log(df1[colname] + 1)
    return df1