import folium
import pandas as pd
from scrape_cloud import get_data  
from geopy.geocoders import Nominatim

def covid_map():
    loc_val = {'Andaman and Nicobar Islands':(11.7401,92.6586),
    'Andhra Pradesh': (15.9240905, 80.1863809),
    'Arunachal Pradesh': (27.6891712, 96.4597226),
    'Assam': (26.4073841, 93.2551303),
    'Bihar': (25.6440845, 85.906508),
    'Chandigarh': (30.7194022, 76.7646552),
    'Chhattisgarh': (21.6637359, 81.8406351),
    'Delhi': (28.6517178, 77.2219388),
    'Goa': (15.3004543, 74.0855134),
    'Gujarat': (22.41540825, 72.03149703699282),
    'Himachal Pradesh' :(31.81676015, 77.34932051968858),
    'Jammu and Kashmir': (33.53155445, 75.3109635338607),
    'Jharkhand': (23.4559809, 85.2557301),
    'Karnataka' :(14.5203896, 75.7223521),
    'Kerala' :(10.3528744, 76.5120396),
    'Ladakh': (33.9456407, 77.6568576),
    'Madhya Pradesh' :(23.9699282, 79.39486954625225),
    'Maharashtra': (19.531932, 76.0554568),
    'Manipur' :(24.7208818, 93.9229386),
    'Meghalaya' :(25.5379432, 91.2999102),
    'Mizoram' :(23.2146169, 92.8687612),
    'Nagaland' :(26.1630556, 94.5884911),
    'Odisha': (20.5431241, 84.6897321),
    'Puducherry' :(11.9340568, 79.8306447),
    'Punjab': (30.9293211, 75.5004841),
    'Rajasthan' :(26.8105777, 73.7684549),
    'Sikkim': (27.601029, 88.45413638680145),
    'Tamil Nadu' :(10.9094334, 78.3665347),
    'Telengana': (17.329125, 78.5822228),
    'Tripura': (23.7750823, 91.7025091),
    'Uttarakhand': (30.091993549999998, 79.32176659343018),
    'Uttar Pradesh': (27.1303344, 80.859666),
    'West Bengal': (22.9964948, 87.6855882),
    'Haryana': (29.0588,76.0856),
    'Dadar Nagar Haveli': (20.1809,73.0169)}

    # def lat_lon(place):
    #     geolocator = Nominatim()
    #     loc = geolocator.geocode(place)
    #     return (loc.latitude,loc.longitude)

    data = get_data()
    # for i in data['state']:
    #     try:
    #         print(i,lat_lon(i))
    #     except:
    #         print(i)

    #print(data)
    map = folium.Map(location= (20.5937,78.9629),zoom_start= 4)
    #data = pd.read_csv('airport_loc.csv')
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)

    folium.LayerControl().add_to(map)

    for (index,row) in data.iterrows():
        
        folium.Marker(location=loc_val[row[0]],
        popup=(row[0]+'\n'+'confirmed cases:'+str(row[3])+'\n'+'Deaths:'+str(row[1])+'\n'+'Cured:'+str(row[2]))
        ).add_to(map)

    return map
