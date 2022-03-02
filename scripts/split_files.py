import pandas as pd
import os

from glob import glob

for file in glob('Twitter/*/*.csv'):
    if os.path.getsize(file) > 100 * 10**6:  # > 100 MB

        filename = os.path.splitext(file)[0]

        for i, chunk in enumerate(pd.read_csv(file, chunksize=500*1000)):  # chunk in files a 500k Tweets
            chunk.to_csv(f'{filename}_{i}.csv', index=False)

        os.remove(file)
