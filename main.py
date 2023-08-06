import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.title('Team Rankings')

# Define initial data
data = {
    'Team Name': ['Goldstein/Seibold', 'Schneider/Seef', 'Leidner/Gator', 'Gutty/Bizz', 'Joey/Misha', 'AA/Dean', 'Ebe/Tumbo', 'Tito/Wil', 'Wein/Rauch', 'Meis/D Rose', 'Alexi/Kuhlkin'],
    'Stock': ['AMC', 'AMC', 'AMC', 'AMC', 'AMC', 'AMC', 'AMC', 'AMC', 'AMC', 'AMC', 'AMC'],
    'Price Bought': [0,0,0,0,0,0,0,0,0,0,0],  # Replace with actual bought prices
    'Current Price': [0, 0, 0,0,0,0,0,0,0,0,0],
    'Gain': [0, 0, 0,0,0,0,0,0,0,0,0]
}

df = pd.DataFrame(data)

def get_current_price(stock):
    ticker = yf.Ticker(stock)
    return ticker.history().tail(1)['Close'].iloc[0]

# Refresh data on button click
if st.button('Update Rankings'):
    for i, row in df.iterrows():
        current_price = get_current_price(row['Stock'])
        df.loc[i, 'Current Price'] = current_price
        df.loc[i, 'Gain'] = ((current_price - row['Price Bought']) / row['Price Bought']) * 100
    # Sorting the DataFrame by 'Gain' column
    df.sort_values('Gain', ascending=False, inplace=True)
    # Resetting the index to get ranking
    df.reset_index(drop=True, inplace=True)

st.table(df.assign(hack='').set_index('hack'))
