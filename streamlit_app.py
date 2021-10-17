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

<<<<<<< HEAD
st.header('SUMMARY')

=======
>>>>>>> 5360d17f76f53185362ec44af0b86d2d190b71ab
col1, col2, col3 = st.columns(3)
col1.metric("Active", "9.7M", "+10%")
col2.metric("Total", "44.6M", "-8%")
col3.metric("Deaths", "719K", "+4%")

<<<<<<< HEAD
url = 'https://drive.google.com/file/d/1D96k1no_9BGQ55YLARWHTyPFf43eOVle/view?usp=sharing'
=======
url = 'https://drive.google.com/file/d/1adjLpmpWc0jOYcVAtjJUyK-6Kdpi8n_V/view?usp=sharing'
>>>>>>> 5360d17f76f53185362ec44af0b86d2d190b71ab
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)
df=df.dropna(how='any')

<<<<<<< HEAD
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
=======

date_selection = st.date_input("Select Date of Search", datetime.date(
    2021, 10, 11), min_value=datetime.date(2020, 1, 21), max_value=datetime.date(2021, 10, 11))
>>>>>>> 5360d17f76f53185362ec44af0b86d2d190b71ab
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
<<<<<<< HEAD
    col1.metric("Total Cases", int(cases_reported))
    col2.metric("Total Deaths", int(float(deaths_reported)))
else:
    st.warning("No Cases Reported")    

=======
    col1.metric("Total Cases(As of Date)", int(cases_reported))
    col2.metric("Deaths", int(float(deaths_reported)))


date_selection1 = st.date_input("Select From Date", datetime.date(
    2020, 1, 21), min_value=datetime.date(2020, 1, 21), max_value=datetime.date(2021, 10, 11))
date_index1= df.index[df['date'] == str(date_selection1)].tolist()

date_selection2 = st.date_input("Select to Date", datetime.date(
    2021, 10, 11), min_value=datetime.date(2020, 1, 21), max_value=datetime.date(2021, 10, 11))
date_index2= df.index[df['date'] == str(date_selection2)].tolist()

# print(len(np.sort(df['fips'].unique())))
# print(df['fips'][date_index2])
>>>>>>> 5360d17f76f53185362ec44af0b86d2d190b71ab
