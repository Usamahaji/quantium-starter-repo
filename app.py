from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. Initialize App
app = Dash(__name__)

# 2. Load Data
try:
    df = pd.read_csv('./data/combined_sales_data.csv')
except:
    df = pd.read_csv('combined_sales_data.csv')
df = df.sort_values(by="date")

# 3. Layout: Clean and Bright
app.layout = html.Div(style={
    'backgroundColor': '#f4f7f9', 
    'minHeight': '100vh',
    'fontFamily': '"Segoe UI", Arial, sans-serif',
    'padding': '40px'
}, children=[

    # Main Card
    html.Div(style={
        'maxWidth': '1100px',
        'margin': '0 auto',
        'backgroundColor': '#ffffff',
        'padding': '30px',
        'borderRadius': '12px',
        'boxShadow': '0 8px 20px rgba(0,0,0,0.05)'
    }, children=[
        
        # Header
        html.Div(style={'textAlign': 'center', 'marginBottom': '30px'}, children=[
            html.H1("Pink Morsel Sales Dashboard", style={'color': '#1a2a6c', 'margin': '0'}),
            html.P("Analyze revenue trends with smooth data transitions", 
                   style={'color': '#5f6368', 'marginTop': '10px'})
        ]),

        # Control Panel
        html.Div(style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'marginBottom': '30px',
            'textAlign': 'center',
            'border': '1px solid #e9ecef'
        }, children=[
            html.Label("SELECT REGION:", 
                       style={'fontWeight': 'bold', 'color': '#1a2a6c', 'display': 'block', 'marginBottom': '15px'}),
            dcc.RadioItems(
                id='region-filter',
                options=[{'label': f' {r.capitalize()}', 'value': r} for r in ['north', 'east', 'south', 'west', 'all']],
                value='all',
                inline=True,
                labelStyle={'marginRight': '25px', 'fontSize': '16px', 'color': '#3c4043'},
                inputStyle={"transform": "scale(1.2)", "marginRight": "8px"}
            ),
        ]),

        # Graph Section
        dcc.Graph(id='sales-line-chart', config={'displayModeBar': False})
    ])
])

# 4. Callback logic with Animation
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    color_map = {
        'north': '#ff4b2b', 'east': '#1a2a6c', 
        'south': '#fdbb2d', 'west': '#22c1c3', 'all': '#6a11cb'
    }
    
    filtered_df = df if selected_region == 'all' else df[df['region'] == selected_region]
    
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        render_mode='svg' # Required for smooth line animations
    )
    
    fig.update_traces(line=dict(color=color_map[selected_region], width=3))
    
    # --- ANIMATION SETTINGS ---
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        transition_duration=800,  # 0.8 seconds of smooth movement
        transition_easing='cubic-in-out', # Starts slow, speeds up, ends slow
        xaxis=dict(showgrid=True, gridcolor='#f0f2f5', title="Timeline"),
        yaxis=dict(showgrid=True, gridcolor='#f0f2f5', title="Total Sales ($)"),
        margin=dict(l=40, r=40, t=20, b=40)
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)