import scrapy
from ..items import LearnItem

class doctorSpider(scrapy.Spider):
    name = 'state'
    start_urls = [
        'https://www.mohfw.gov.in/'
    ]

    def parse(self,response):
        data = response.css('table.table tr td::text').extract()
        items = LearnItem()
        ind = data[::5]
        state = data[1::5]
        cnf_cases = data[2::5]
        cured = data[3::5]
        death = data[4::5]
        for i in range(len(ind)-1): 
            items['index']=ind[i]
            items['state']=state[i]
            items['confirmed_cases']=cnf_cases[i]
            items['cured']=cured[i]
            items['death']=death[i]
            yield items