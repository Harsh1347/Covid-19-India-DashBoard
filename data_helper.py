import json
import requests
import pandas as pd
from matplotlib import pyplot as plt


def state_coding():
    data_req = requests.get('https://api.covid19india.org/data.json')
    data_req = data_req.json()
    state_data = data_req['statewise']
    state_code = {}
    for state in state_data:
        state_code[state['state']] = state['statecode']
    return state_code

def state_wise_data():
    state_wise = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    cnf_case = state_wise.loc[state_wise['Status']=='Confirmed']
    cured = state_wise.loc[state_wise['Status']=='Recovered']
    death = state_wise.loc[state_wise['Status']=='Deceased']
    del(cnf_case['Status'])
    del(cured['Status'])
    del(death['Status'])
    l = list(cured['Date'])
     
    cnf_case_cum,cured_cum,death_cum = cnf_case.cumsum(),cured.cumsum(),death.cumsum()
    del(cnf_case_cum['Date'])
    del(cured_cum['Date'])
    del(death_cum['Date'])
    cnf_case_cum['Date'] = l
    cured_cum['Date']= l
    death_cum['Date']= l
    return cnf_case,cured,death,cnf_case_cum,cured_cum,death_cum
   
def get_states_statecode():
    state_dict = state_coding()
    return list(state_dict.keys()),list(state_dict.values())

