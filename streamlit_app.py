from attr import s
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pydeck as pdk
from geopy.geocoders import Nominatim
import time
from pprint import pprint

app = Nominatim(user_agent="tutorial")

st.set_page_config(layout="wide")

st.title("""US COVID ANALYSIS""")

st.header('SUMMARY')

col1, col2, col3 = st.columns(3)
col1.metric("Active", "9.7M", "+10%")
col2.metric("Total", "44.6M", "-8%")
col3.metric("Deaths", "719K", "+4%")

url = 'https://drive.google.com/file/d/1D96k1no_9BGQ55YLARWHTyPFf43eOVle/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)
df=df.dropna(how='any')

########SCATTER PLOT OF COUNTY WISE

st.header('MAP OF CASES')

date_selection1 = st.date_input("Select Date", datetime.date(
    2021, 1, 21), min_value=datetime.date(2020, 6, 16), max_value=datetime.date(2021, 10, 11))
date_index1= df.index[df['date'] == str(date_selection1)].tolist()

dfscatter=df[['lat','lon']]
dfscatter = dfscatter.filter(items = date_index1, axis=0)
st.map(dfscatter)

####### DAY WISE ANALYSIS FOR EACH COUNTY

st.header('TOTAL SUMMARY FOR EACH COUNTY')

date_selection = st.date_input("Select Date", datetime.date(
    2020, 10, 11), min_value=datetime.date(2020, 6, 16), max_value=datetime.date(2021, 10, 11))
date_index = df.index[df['date'] == str(date_selection)].tolist()

state_option = st.selectbox('Select State', np.sort(df['state'].unique()))

statewise_county = df.index[df['state'] == state_option].tolist()

county_option = st.selectbox('Select County', np.sort(
    df['county'][statewise_county].unique()))
county_index = df.index[df['county'] == county_option].tolist()

list1_as_set = set(date_index)
intersection = list1_as_set.intersection(county_index)

cases_reported = df['cases'][intersection].astype(str).values
deaths_reported = df['deaths'][intersection].astype(str).values

if cases_reported:
    col1, col2 = st.columns(2)
    col1.metric("Total Cases", int(cases_reported))
    col2.metric("Total Deaths", int(float(deaths_reported))),
else:
    st.warning("No Cases Reported")    

#### LINE PLOT