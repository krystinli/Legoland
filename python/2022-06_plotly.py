
# 1) Using plotly.express
import plotly.express as px

df = px.data.stocks() # sample data
fig = px.line(df, x='date', y="GOOG")
fig.show()

# 2) Using graph_objects
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df.head()

fig = go.Figure(
    [go.Scatter(
        x=df['Date'],
        y=df['AAPL.High']
        )]
    )
fig.show()

# 3) Different Chart Types on Date Axes
df = px.data.stocks(indexed=True)-1
df.head()

# bar chart
fig = px.bar(df, x=df.index, y="GOOG")
fig.show()

# area chart
fig = px.area(df, facet_col="company", facet_col_wrap=2)
fig.show()
