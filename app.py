from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 

# Initialise the Dash app 
app = Dash(__name__)

# Load and sort the data 
df = pd.read_csv('./data/combined_sales_data.csv')
df = df.sort_values(by='date')

# Create the line chart 
# This chart will show sakes on the Y axis and date n the X axis 
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Trend")

# Define the layout of the webpage 
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Visualiser', style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])
# Run the app 
if __name__=='__main__':
    app.run(debug=True)