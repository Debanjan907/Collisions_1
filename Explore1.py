###########
# Bounding box of New york City :
#  40.917577, -74.25909,
#  40.477399, -73.70000
############
# Radius of earth 6371.009 Km
# Units used for geographical distance : Km
############
#TODO: Use bigfloat


import math
import numpy as np;

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
        dist = self.R * math.sqrt( self.degrees_to_radians_aux(dlat)**2 + (math.cos(self.degrees_to_radians_aux(mean_lat))*self.degrees_to_radians_aux(dlon))**2 )
        return dist;









