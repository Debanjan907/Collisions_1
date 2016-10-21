###########
# Bounding box of New york City :
#  40.917577, -74.25909,
#  40.477399, -73.70000
############
# Radius of earth 6371.009 Km
# Units used for geographical distance : Km
############
#TODO: Use bigfloat

import csv
import math
import numpy as np;
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

class location :
    lat=0;
    lon=0;
    R = 6371.009
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

    def degrees_to_radians_aux(self,value):
        return (value * math.pi)/180;

    #return distance between the location,and another location point(object)
    def distance(self,loc2):
        dlon = abs( loc2.lon - self.lon )
        dlat = abs( loc2.lat - self.lat )
        mean_lat = (self.lat + loc2.lat)/2;
        dist = self.R * math.sqrt( self.degrees_to_radians_aux(dlat)**2 +
                                   (math.acos(self.degrees_to_radians_aux(mean_lat))*self.degrees_to_radians_aux(dlon))**2 )
        return dist;



def plot_basic_map(city):

    # 40.917577, -74.25909,
    # 40.477399, -73.70000
    my_map = Basemap(projection='merc',
                     resolution='h',
                     lat_0=40.5,
                     lon_0=-73.7,
                     llcrnrlat=40.0,
                     llcrnrlon=-74.4,
                     urcrnrlat=41.0,
                     urcrnrlon=-73.0)


    my_map.fillcontinents(color='yellow')
    my_map.drawmapboundary(fill_color='aqua')
    my_map.drawcoastlines()
    my_map.drawcountries()
    return my_map;

def plot_points( city, year ,map_obj) :
    Filename =  city + '_' + str(year) + '.csv'
    x = []
    y = []
    with open(Filename, 'r') as csvfile:
        rd = csv.reader(csvfile)
        for row in rd:
            x.append(float(row[2])) #latitude
            y.append(float(row[3])) #longitude

    for i in range(len(x)) :
        lon = y[i]
        lat = x[i]
        x1,y1 = map_obj(lon, lat)
        map_obj.plot(x1,y1, marker ='o', markersize = 1, color ='m')


map_obj = plot_basic_map('nyc')
plot_points('nyc', 2014, map_obj)
plt.show()
