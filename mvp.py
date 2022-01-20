#Imports
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("marks vs days_pre.csv")
x = df["Days Present"].tolist()
y = df["Marks In Percentage"].tolist()

fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage", color = "Roll No")
fig.show()

corrcoef = np.corrcoef(x, y)
print(corrcoef[0][1])