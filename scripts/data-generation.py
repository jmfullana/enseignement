# iport PAndas
import pandas as pd

# data generation
x=np.linspace(0,5)
y1 = np.power(x,0.5)
y2 = np.power(x,0.25)

# Pandas series
sx = pd.Series(x)
sy1 = pd.Series(y1)
sy2 = pd.Series(y2)

# Concat data in columns
nd = pd.concat([sx,sy1,sy2],axis=1)

# Write data
nd.to_csv("test.csv")

# Read data
d = pd.read_csv("test.csv",delimiter=",")
print(d)
