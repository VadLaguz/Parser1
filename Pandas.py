import pandas as pd
import os, glob
df = pd.read_csv('data/0_Баранина_и_дичь.csv')
df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('data', "*.csv"))))
df.to_csv('Prod_InfoDF.csv', index=False)

