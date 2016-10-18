# Read data from CSV file
import csv

##############################
# set year
YEAR = 2016
# set filename
Filename = 'NYPD_Motor_Vehicle_Collisions_1.csv';
# set city
City = 'nyc'
##############################
# File format :
# 0 Date
# 1 Time
# 4 Latitude
# 5 Longitude
# 10 Total Injury
# 11 Total Killed
# 12 Ped Injured
# 13 Ped Killed
# 14 Cyc Injured
# 15 Cyc Killed
# 16 Motorist Injured
# 17 Motorist Killed
##############################

lat_lon_box = dict();
lat_lon_box['nyc'] = [40.917577, -74.25909, 40.477399, -73.70000]


data_by_year = dict()



class lat_long_validator:
    city = '';
    min_lat = 0;
    max_lat = 0;
    min_lon = 0;
    max_lat = 0;

    def __init__(self,city):
        self.city = city
        self.set_validation_bounds();

    def set_validation_bounds(self):
        city = self.city;
        if lat_lon_box[city][2] < lat_lon_box[city][0] :
            self.min_lat = lat_lon_box[city][2]
            self.max_lat = lat_lon_box[city][0]
        else:
            self.min_lat = lat_lon_box[city][0]
            self.max_lat = lat_lon_box[city][2]

        if lat_lon_box[city][1] < lat_lon_box[city][3]:
            self.min_lon = lat_lon_box[city][1]
            self.max_lon = lat_lon_box[city][3]
        else:
            self.min_lon = lat_lon_box[city][3]
            self.max_lon = lat_lon_box[city][1]
        print ( "Min Lat" +str(self.min_lat) + " Max Lat:" + str(self.max_lat) + " Min Lon"+ str(self.min_lon) +" Max Lon"+ str(self.max_lon))


    def validate(self,lat,lon):
        #check if empty
        if not lat or not lon:
            return False;

        #convert from String to Float
        lat = float(lat)
        lon = float(lon)

        if  lat < self.min_lat or lat > self.max_lat :
            return False;
        if lon < self.min_lon or lon > self.max_lon:
            return False;
        return True;


def validate_year(date):
    # format "mm/dd/yyyy"
    parts = date.split('/')
    return int(parts[2]) == YEAR;


loc_validator = lat_long_validator('nyc')
with open(Filename, 'r') as csvfile:
    rd = csv.reader(csvfile)
    count = 0;
    row_count =0;
    for row in rd:
        count += 1;
        #omit the 1st row
        if count == 1 :
            continue;

        # count till 10 records...TODO Remove!!!!
        if count > 10000 :
            break;

        #Validate year
        if not validate_year(row[0]):
            continue;
        year = YEAR;
        time = row[1]
        lat = row[4]
        lon = row[5]

        # check if empty
        if not lat or not lon:
            continue;
        lat = float(row[4])
        lon = float(row[5])

        if not loc_validator.validate(lat,lon):
            continue;

        death_or_injury = int(row[10]) + int(row[11]);
        print (row[0]+" "+time+"  Lat :" + str(lat) + " Long:" + str(lon) + "  Death/Injury : "+ str(death_or_injury))
        row_count +=1
        current = []
        current.append(row[0])
        current.append(time)
        current.append(lat)
        current.append(lon)
        current.append(death_or_injury)
        if year not in data_by_year or (data_by_year[year] is None):
            data_by_year[year] = []

        data_by_year[year].append(current)

print(row_count)
print(data_by_year)






