# Covid 19 India DashBoard
<ul>
<li>A spider has been created to scrape the live data from www.mohfw.gov.in and deployed on ScrapingHub.The spider runs everyday at a specified time to scrape the data and stores it in Scapy Cloud.
</li>scrape_cloud.py gets the data from Scrapy Cloud and converts it into pandas data frame.
</li>maps.py uses the folium lib to create a map and adds a popup which has the information of death, cured and confirmed cases.
</li>dash.py uses streamlit to create a web app.
</ul>
![Object_tracking](https://github.com/Harsh1347/Covid-19-India-DashBoard/blob/master/covid-dash.gif)
