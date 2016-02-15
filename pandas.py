import pandas as pd

# df = DataFrame - reading the csv
df = pd.read_csv('single.csv')

#Data Frame should be group by column
groups = df.groupby('ID', as_index=False)

for name, data in groups:
    name = name.replace('/', '-')
    data.to_csv('{}.csv'.format(name), index=False)