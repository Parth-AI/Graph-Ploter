import pandas as pd

import plotly.express as px

#data = [123,15]
df = pd.read_csv("Data.csv")
fig = px.scatter(df, x='Population', y='InternetUsers', title="Internet User", color='Country', size = 'Percentage', size_max = 60)
fig.show()