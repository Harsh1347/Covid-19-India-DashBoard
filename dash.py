import streamlit as st
from maps import covid_map
from scrape_cloud import get_data
import pandas as pd 

co_map = covid_map()
data=get_data()
data['death'] = data.death.astype('int')
data['cured'] = data.cured.astype('int')
data['confirmed_cases'] = data.confirmed_cases.astype('int')

data.loc[35] = ['Total',data.death.sum(), data.cured.sum(), data.confirmed_cases.sum()]
st.title("COVID-19 INDIA ANALAYSIS")
st.text("COVID MAP")
st.write(co_map._repr_html_(), unsafe_allow_html=True)
st.table(data)
data['death'] = data.death.astype('int')
data['cured'] = data.cured.astype('int')
data['confirmed_cases'] = data.confirmed_cases.astype('int')
# st.text(data.death.sum())
# st.text(data.cured.sum())
# st.text(data.confirmed_cases.sum())
