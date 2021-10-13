import streamlit as st
import pandas as pd
import numpy as np
import requests
from io import StringIO

st.set_page_config(layout="wide")
st.write("""My First APP""")

# data=pd.read_csv(r"C:\Users\supreethbare\Downloads\day_wise.csv")
# # print(len(data))
url='https://drive.google.com/file/d/1G2AVl-ANLHHkwMqyGkqCwJcFeb_zLlJz/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)
st.write("""len(df)""")
