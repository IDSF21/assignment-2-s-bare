import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.write("""My First APP""")

data=pd.read_csv(r"C:\Users\supreethbare\Downloads\day_wise.csv")
# print(len(data))
st.write("""len(data)""")

# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis="columns", inplace=True)
#     data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
#     return data