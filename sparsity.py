### Calculates sparsity of each numerical feature in a pandas dataframe and returns a dictionary for all the features along with their sparsity

def sparsity(df):
    sparsity_all = {}
    for colname in df.columns.values:
        sparsity_ = float(len(list(filter(lambda x: float(x) == 0.0,  df[colname]))))/df[colname].shape[0]
        sparsity_all[colname] = str(int(sparsity_*100)) + '%'
    return sparsity_all