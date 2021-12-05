import streamlit as st
import pandas as pd
import numpy as np
import csv


vd1 = "C:/Users/Han/.conda/envs/env38/port_analysis_test3.csv"
viewdata1 = pd.read_csv(vd1)


st.title("3RD SIG ANALYTICS", anchor=None)
st.header("Port & Trade Analysis from Shipping Logistics Data", anchor=None)

st.write("Dashboard prepared by: [Han Lin](https://www.linkedin.com/in/han-lin-a906b6136/)")


df1 = pd.DataFrame(viewdata1)


section2 = df1.groupby(['Date_Obs', 'Location', 'Vessel_Type', 'Vessel_Name', 'IMO', 'MMSI', 'lon', 'lat'])


map_data = pd.DataFrame(viewdata1, columns=['lat', 'lon'])
st.map(map_data)



sorted_sector_unique = sorted( df1['Location'].unique() )
selected_sector = st.multiselect('Location', sorted_sector_unique, sorted_sector_unique)

df_selected_sector = df1[ (df1['Location'].isin(selected_sector)) ]

st.dataframe(df_selected_sector)


metric1 = st.sidebar.metric(label="Total in Port", value=len(pd.DataFrame(df_selected_sector)))

dateselect = st.sidebar.date_input('Select Date')
textselect = st.sidebar.text_input('Select Vessel')
imoselect = st.sidebar.text_input('Select IMO')
mmsiselect = st.sidebar.text_input('Select MMSI')



