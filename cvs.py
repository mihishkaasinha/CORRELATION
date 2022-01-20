#Imports
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("coffee vs sleep.csv")
x = df["Coffee in ml"].tolist()
y = df["sleep in hours"].tolist()

fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours", color = "week")
fig.show()

corrcoef = np.corrcoef(x, y)
print(corrcoef[0][1])