import numpy as np
import pandas as pd

np.random.seed(0)

df = pd.DataFrame(np.random.uniform(100, size=(10000, 3)), columns=list('abh'))

df['P'] = df.apply(lambda row: 1/2 * (row.a + row.b) * row.h, axis=1)

df.to_csv('data.csv', index=False)