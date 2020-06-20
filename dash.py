import streamlit as st
from maps import covid_map
from scrape_cloud import get_data
from data_helper import state_coding,state_wise_data 
import pandas as pd
from matplotlib import pyplot as plt 

@st.cache
def codes():
    s_coding = state_coding()
    return s_coding

@st.cache
def daily_data():
    c,r,d,cc,cr,cd = state_wise_data()
    return c,r,d,cc,cr,cd
s_coding = codes()

co_map = covid_map()

data=get_data()

cn,cr,d,ccn,ccr,cd = daily_data()

data['death'] = data.death.astype('int')
data['cured'] = data.cured.astype('int')
data['confirmed_cases'] = data.confirmed_cases.astype('int')

data.loc[len(data['cured'])] = ['Total',data.death.sum(), data.cured.sum(), data.confirmed_cases.sum()]
st.title("COVID-19 INDIA ANALAYSIS")

sel = st.sidebar.radio('NAVIGATION',('Home','State Wise Data','Visualization'))

if sel == 'Home':
    st.write("<h3>COVID MAP</h3>",unsafe_allow_html=True)
    st.write(co_map._repr_html_(), unsafe_allow_html=True)
    st.write("<h3>Today</h3>",unsafe_allow_html=True)
    #st.table(data.loc[data['state']=='Total'])
    tab_d = {'Total Confirmed Cases':cn['TT'][-1:].values,'Recovered':cr['TT'][-1:].values,'Deaths':d['TT'][-1:].values}
    st.table(tab_d)
    st.write("<h3>Overall</h3>",unsafe_allow_html=True)
    tab = {'Total Confirmed Cases':ccn['TT'][-1:].values,'Recovered':ccr['TT'][-1:].values,'Deaths':cd['TT'][-1:].values}
    st.table(tab)
    inc = ccn['TT'][-1:].values - ccn['TT'][-2:-1].values
    
    st.success(f"India has a recovery rate of {round(((ccr['TT'][-1:].values /ccn['TT'][-1:].values)*100)[0],1) }%")
    st.warning(f"There has been increase of {inc[0]} cases in last 24 hours in India")
    st.error(f"{(cd['TT'][-1:].values - cd['TT'][-2:-1].values)[0]} deaths have been reported in last 24 hours in India")
    

if sel == 'State Wise Data':
    op = st.radio('Select an option',('All State','Particular State'))
    if(op == 'All State'):
        st.table(data)

    if(op=='Particular State'):
        selected_state = st.selectbox('select a state',data['state'],)
        st.table(data.loc[data['state']==selected_state])

if sel == 'Visualization':
    
    option = list(s_coding.keys())
    l = list(cn.Date)
    l = [i[:-3] for i in l]
    l = [i.replace('-','') for i in l]
    cumsum_today = st.radio('Select an option',('Cumulative','Daily'))
    dur = st.radio('Select Duration',('Last 7 Days','Last 15 Days','Last 30 Days','All'))
    
    if dur == 'Last 7 Days':
        t= -7
    if dur == 'All':
        t= 0
    if dur == 'Last 30 Days':
        t=-30
    if dur == 'Last 15 Days':
        t=-15
    selected_state = st.selectbox('select a state',sorted(option))
    plt.style.use('fivethirtyeight')
    rot = 60
    if cumsum_today == 'Daily':
        cn[s_coding[selected_state]][t:].plot(label = 'Confirmed')
        plt.xticks(cn.index[t:],l[t:],rotation = rot,fontsize=6)
        plt.yticks(fontsize = 8)
        plt.ylim(0)
        plt.title(f"Confirmed cases in {selected_state}",fontsize = 15)
        st.pyplot()

        cr[s_coding[selected_state]][t:].plot(label = 'Cured',color ='green')
        plt.xticks(cn.index[t:],l[t:],rotation = rot,fontsize=6)
        plt.yticks(fontsize = 8)
        plt.ylim(0)
        plt.title(f"Cured Patients in {selected_state}",fontsize = 15)
        st.pyplot()
        
        d[s_coding[selected_state]][t:].plot(label = 'Deaths',color ='red' )
        plt.xticks(cn.index[t:],l[t:],rotation = rot,fontsize=6)
        plt.yticks(fontsize = 8)
        plt.ylim(0)
        plt.title(f"Deaths in {selected_state}",fontsize = 15)
        st.pyplot()

    if cumsum_today == 'Cumulative':
        ccn[s_coding[selected_state]][t:].plot(label = 'Confirmed')
        plt.xticks(cn.index[t:],l[t:],rotation = rot,fontsize=6)
        plt.yticks(fontsize = 8)
        plt.ylim(0)
        plt.title(f"Confirmed cases in {selected_state}",fontsize = 15)
        st.pyplot()

        ccr[s_coding[selected_state]][t:].plot(label = 'Cured',color ='green')
        plt.xticks(cn.index[t:],l[t:],rotation = rot,fontsize=6)
        plt.yticks(fontsize = 8)
        plt.ylim(0)
        plt.title(f"Cured Patients in {selected_state}",fontsize = 15)
        st.pyplot()
        
        cd[s_coding[selected_state]][t:].plot(label = 'Deaths',color ='red' )
        plt.xticks(cn.index[t:],l[t:],rotation = rot,fontsize=6)
        plt.yticks(fontsize = 8)
        plt.ylim(0)
        plt.title(f"Deaths in {selected_state}",fontsize = 15)
        st.pyplot()
    
    
 
    




