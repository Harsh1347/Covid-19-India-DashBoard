from scrapinghub import ScrapinghubClient
import pandas as pd

def get_data():
    client = ScrapinghubClient('<APIKEY>')
    project = client.get_project(<Project ID>)
    #print(project.spiders.list())
    spider = project.spiders.get('state')
    job_id = list(project.activity.iter(count=2))
    job_id = job_id[1]['job']
    job = client.get_job(job_id)

    state_name = []
    death =[]
    cured =[]
    confirmed_cases=[]
    for item in job.items.iter():
        state_name.append(item[b'state'].decode("utf-8"))
        death.append(item[b'death'].decode("utf-8"))
        cured.append(item[b'cured'].decode("utf-8"))
        confirmed_cases.append(item[b'confirmed_cases'].decode("utf-8"))

    data = {'state':state_name,'death':death,'cured':cured,'confirmed_cases':confirmed_cases}
    data = pd.DataFrame(data)
    data = data[:-1]
    #data.to_csv('corona_data.csv')
    return data

