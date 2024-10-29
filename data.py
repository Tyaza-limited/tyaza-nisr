import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

excel_file = pd.ExcelFile('RW_Quarterly_LFS_Tables_2024Q2.xlsx')

dfs = {}

for sheet_name in excel_file.sheet_names:
    dfs[sheet_name] = pd.read_excel(excel_file, sheet_name=sheet_name)

data = dfs['LFIndicatorsYouthAdult']


dd = data.drop(index=[0,1,2]+list(range(13, 28))).T


def generate_dates(start_year, end_year):
    dates = []
    for year in range(start_year, end_year + 1):
        for quarter in ['Q1', 'Q2', 'Q3', 'Q4']:
            if(year == 2024 and (quarter == 'Q3' or quarter == 'Q4')):
                continue
            dates.append(f"{year} - {quarter}")
    return dates

dates = generate_dates(2019, 2024)

columns = dd.iloc[0].values.tolist()
dd = dd[1:]


def d_graph():
    figs=dict()
    for col in dd:
        data = dict()
        data['Date'] = dates
        data[columns[col - 3]] = dd[col]
        df = pd.DataFrame(data)
        fig = px.line(df, x='Date', y=[columns[col - 3]],
                               labels={'value': 'Individuals', 'variable': columns[col - 3]},
                title= columns[col - 3] +' Increase Over Time in Rwanda')

       
        fig.update_traces(mode='lines+markers') 
        figs[columns[col - 3]]=fig
    
    return figs


year_2019 = dd[:4]
year_2020 = dd[4:][:4]
year_2021 = dd[8:][:4]
year_2022 = dd[12:][:4]
year_2023 = dd[16:][:4]
year_2024 = dd[20:][:4]


def line_graphs_for_trends_over_time():
    # Create a DataFrame with the relevant data
    data = {
        'Date': dates,
        'Labour force participation rate(%)': dd[3],
        'Employment-to-population ratio(%)': dd[4],
        'LU1-Unemployment rate (%)': dd[7]
    }
    
    df = pd.DataFrame(data)

    # Create a line graph with all three indicators
    fig = px.line(
        df,
        x='Date',
        y=['Labour force participation rate(%)', 
           'Employment-to-population ratio(%)', 
           'LU1-Unemployment rate (%)'],
        labels={
            'value': 'Percentage (%)',
            'variable': 'Indicators'
        },
        title='Labour Force Indicators Over Time'
    )

    # Update trace settings for better visualization
    fig.update_traces(mode='lines+markers') 
    fig.update_layout(legend_title_text='Indicators')
    return fig


def bar_charts_for_comparison(dates, dd):
    data = {
        'Date': dates,
        'Rate of Population Outside the Labour Force (%)': dd[5],
        'NEET Rate (%)': dd[11],
        'Median Monthly Earnings at Main Job': dd[12]
    }
    
    df = pd.DataFrame(data)

    # Create subplots
    fig = make_subplots(rows=1, cols=3, subplot_titles=[
        'Rate of Population Outside the Labour Force (%)',
        'NEET Rate (%)',
        'Median Monthly Earnings at Main Job'
    ])
    
    # Add each bar chart to a subplot
    fig.add_trace(
        go.Bar(x=df['Date'], y=df['Rate of Population Outside the Labour Force (%)'], name='Rate of Population Outside the Labour Force (%)', width=0.3),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=df['Date'], y=df['NEET Rate (%)'], name='NEET Rate (%)', width=0.3),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Bar(x=df['Date'], y=df['Median Monthly Earnings at Main Job'], name='Median Monthly Earnings at Main Job', width=0.3),
        row=1, col=3
    )
    
    # Update layout
    fig.update_layout(
        title_text='Comparison of Labour Indicators',
        showlegend=False,
        height=400,
        xaxis_title='Year/Quarter',
        yaxis_title='Value'
    )
    
    # Update axes for better visibility
    for i in range(1, 4):
        fig.update_xaxes(title_text='Year/Quarter', row=1, col=i)
        fig.update_yaxes(title_text='Value', row=1, col=i)
    
    return fig
