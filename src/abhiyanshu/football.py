

import pandas as pd

football = pd.read_csv(r"C:\Users\Abhiyanshu\Downloads\archive(4)\appearances.csv")
print(football.head())

print(football.info())

# Shows all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(football)

# Remove duplicates
print(football.drop_duplicates(inplace=True))

#dropped columns
drop_cloumns = football.drop(['xGoalsChain','xGoalsBuildup'],axis=1)
print(drop_cloumns)

football['assists'] = football['assists'].fillna()
football_na = football.dropna()
print(football_na)


