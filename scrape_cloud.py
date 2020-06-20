from scrapinghub import ScrapinghubClient
import pandas as pd

def get_data():
    client = ScrapinghubClient('2818dd084edb4c36afc5b5460f86b0e6')
    project = client.get_project(441598)
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
    return data

