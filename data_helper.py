import json
import requests
import pandas as pd
from matplotlib import pyplot as plt


def state_coding():
    a = requests.get('https://api.covid19india.org/data.json')
    a = a.json()
    a = a['statewise']
    state_code = {}
    for i in a:
        state_code[i['state']] = i['statecode']
    return state_code

def state_wise_data():
    state_wise = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    cnf_case = state_wise.loc[state_wise['Status']=='Confirmed']
    cured = state_wise.loc[state_wise['Status']=='Recovered']
    death = state_wise.loc[state_wise['Status']=='Deceased']
    del(cnf_case['Status'])
    del(cured['Status'])
    del(death['Status'])
    return cnf_case,cured,death,cnf_case.cumsum(),cured.cumsum(),death.cumsum()


