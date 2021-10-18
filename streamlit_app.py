import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pydeck as pdk

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
    2020, 6, 30), min_value=datetime.date(2020, 6, 17), max_value=datetime.date(2021, 10, 11))
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

cases_reported=cases_reported[0]
deaths_reported=deaths_reported[0]

if int(cases_reported)>0:
    col1, col2 = st.columns(2)
    col1.metric("Total Cases", int(cases_reported))
    col2.metric("Total Deaths", int(float(deaths_reported)))
else:
    st.warning("No Cases Reported")    

#### BAR GRAPH

st.header('Hot Spots')

date_selection = st.date_input("Choose Date for Total cases", datetime.date(
    2020, 6, 21), min_value=datetime.date(2020, 6, 16), max_value=datetime.date(2021, 10, 11))
date_index = df.index[df['date'] == str(date_selection)].tolist()
st.write("As of Date:",date_selection)

options = st.multiselect(
     'Select Cities',
     np.sort(
    df['county'].unique()),
     ['Pittsburg','San Francisco','San Diego','Dallas','Miami','Los Angeles'])

county_index = df.index[df['county'].isin(options)].tolist()

list1_as_set = set(date_index)
intersection = list1_as_set.intersection(county_index)

st.write("TOTAL CASES")



county_dict=dict(zip(df['county'][intersection],df['cases'][intersection]))

bar_df=pd.DataFrame.from_dict(county_dict,orient='index')

st.bar_chart(bar_df,height=500)

st.write("TOTAL DEATHS")

options = st.multiselect(
     'Select Cities (Deaths)',
     np.sort(
    df['county'].unique()),
     ['Pittsburg','San Francisco','San Diego','Dallas','Miami','Los Angeles'])

county_index = df.index[df['county'].isin(options)].tolist()

list1_as_set = set(date_index)
intersection = list1_as_set.intersection(county_index)

death_dict=dict(zip(df['county'][intersection],df['deaths'][intersection]))

death_pd=pd.DataFrame.from_dict(death_dict,orient='index')

st.bar_chart(death_pd,height=500)


###########  LINE

st.header('CASE SPIKES')

st.write("Over the entire period")

state_option = st.selectbox('State', np.sort(df['state'].unique()))

statewise_county = df.index[df['state'] == state_option].tolist()

county_option = st.selectbox('County Wise Graph', np.sort(
    df['county'][statewise_county].unique()))
county_index = df.index[df['county'] == county_option].tolist()

new_cases=[]
temp=0
for i,j in enumerate(county_index):
    if i>0:
        new=df['cases'][j]-df['cases'][temp]
        if new<0:
            new=0
        new_cases.append(new)
    temp=j

st.line_chart(new_cases)
new_cases=[]

st.header('DEATH SPIKES')

st.write("Over the entire period")
new_deaths=[]
temp=0
for i,j in enumerate(county_index):
    if i>0:
        new=df['deaths'][j]-df['deaths'][temp]
        if new<0:
            new=0
        new_deaths.append(new)
    temp=j

st.line_chart(new_deaths)
new_deaths=[]

