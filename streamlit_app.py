from attr import s
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pydeck as pdk



st.set_page_config(layout="wide")

st.title("""US COVID ANALYSIS""")

col1, col2, col3 = st.columns(3)
col1.metric("Active", "9.7M", "+10%")
col2.metric("Total", "44.6M", "-8%")
col3.metric("Deaths", "719K", "+4%")

# data=pd.read_csv(r"C:\Users\supreethbare\Downloads\day_wise.csv")
# # print(len(data))
url='https://drive.google.com/file/d/1adjLpmpWc0jOYcVAtjJUyK-6Kdpi8n_V/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)

date_selection = st.date_input("Select Date of Search",datetime.date(2021,10,11),min_value=datetime.date(2020,1,21), max_value=datetime.date(2021,10,11))
date_index=df.index[df['date']==str(date_selection)].tolist()

state_option = st.selectbox('Select State',np.sort(df['state'].unique()))

statewise_county = df.index[df['state']==state_option].tolist()

county_option = st.selectbox('Select County',np.sort(df['county'][statewise_county].unique()))
county_index=df.index[df['county']==county_option].tolist()

list1_as_set = set(date_index)
intersection = list1_as_set.intersection(county_index)

cases_reported=df['cases'][intersection].astype(str).values
deaths_reported=df['deaths'][intersection].astype(str).values


col1, col2 = st.columns(2)
col1.metric("Cases", int(cases_reported))
col2.metric("Deaths",int(float(deaths_reported)))

row1_1, row1_2 = st.columns((2,3))

with row1_1:
    st.title("CASE GRAPH")
    month_selected = st.select_slider('Select a color of the rainbow',options=['January', 'Febraury', 'March', 'May', 'June', 'July', 'August','September','October','November','December'])


with row1_2:
    st.write(
    """
    ##
    Examining how COVID cases varied over time in US and at its statewise counties.
    By sliding the slider on the left you can view different slices of time and explore different covid trends.
    """)

def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))    

washington = [32.318230, -86.902298]
california = [36.778261, -119.417932]
cases_reported=df['cases'][intersection].to_frame()

print(cases_reported)



row2_1, row2_2 = st.columns((2))

with row2_1:
    map(cases_reported, washington[0], washington[1], 12)

with row2_2:
    map(cases_reported, california[0], california[1], 12)