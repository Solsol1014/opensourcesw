import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(3, 2))

dff = pd.DataFrame(np.random.rand(3, 2), index=['m1', 'm2', 'm3'], columns=['price', 'num'])

print(df)
print(dff, '\n')
print(dff['num'], '\n')
print(dff['num']>0.5, '\n')
dff2 = dff[dff['num']>0.5]
print(dff2, '\n')
print(dff2['num'], '\n')
print(dff.T)