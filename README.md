# Covid 19 India DashBoard
<ul>
<li>A spider has been created to scrape the live data from www.mohfw.gov.in and deployed on <a href = 'https://scrapinghub.com/'>ScrapingHub</a>.The spider runs everyday at a specified time to scrape the data and stores it in Scapy Cloud. The App also uses the https://api.covid19india.org/ api for data.
<li>scrape_cloud.py gets the data from Scrapy Cloud and stores it into pandas data frame.
<li>maps.py uses the folium lib to create a map and adds a popup which has the information of death, cured and confirmed cases.
<li>dash.py uses streamlit to create a web app.
</ul>

The dashboard has been deployed on Heroku : https://india-covid19-dash.herokuapp.com/

![COVID-19 INDIA DASH BOARD](https://github.com/Harsh1347/Covid-19-India-DashBoard/blob/master/covid-dash.gif)

More functionalities to be added soon
