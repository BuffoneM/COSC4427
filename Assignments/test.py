import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(9., 18.).reshape((3, 3)), 
                   columns=list('bst'),
                   index=['Brampton', 'Sault Ste. Marie', 'Timmins'])

df2 = pd.DataFrame(np.arange(6.).reshape((2, 3)), 
                   columns=list('bst'),
                   index=['Brampton', 'Scarborough'])

print(df1+df2)