import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import finnhub

st.title('Team Rankings')

# Define initial data
data = {
    'Team Name': ['Goldstein/Seibold', 'Schneider/Seef', 'Leidner/Gator', 'Gutty/Bizz', 'Joey/Misha', 'AA/Dean', 'Ebe/Tumbo', 'Tito/Wil', 'Wein/Rauch', 'Meis/D Rose', 'Liffman/Kuhlkin', 'Galper/Garber'],
    'Stock': ['AMC', 'AAL', 'UPS', 'PLTR', 'AAL', 'SOXL', 'RL', 'LCID', 'TDS', 'WYNN', 'SWKS', 'MF'],
    'Price Bought': [4.93,15.84,180.94,18.20,15.84,24.88,131.74,6.62,14.84,104.18,109.30,1.98], # Fill in with actual bought prices
    'Current Price': [0.0]*12,
    'Gain': [0.0]*12
}

df = pd.DataFrame(data)

def get_current_price(stock):
    finnhub_client = finnhub.Client(api_key="cj819ehr01qkj2usugjgcj819ehr01qkj2usugk0")
    return finnhub_client.quote(stock)['c']

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

net_gain = df['Gain'].sum()

# Use Streamlit's st.write() function to display the result based on the net_gain value
if net_gain > 0:
    st.write("Net Gain:", net_gain)
else:
    st.write("Net Loss:", net_gain)


