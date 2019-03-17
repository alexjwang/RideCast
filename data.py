import pandas as pd
import numpy as np
import random
from math import sin, cos, sqrt, atan2, radians

# Import data
def readadddata(filename):
    data = pd.read_csv(filename)
    data = data.drop(['Base'], 1)
    datetimes = data['Date/Time']
    dayofweek = []
    hour = []
    for s in datetimes:
        day = int(s.split('/')[1])%7
        dayofweek.append(day)
        time = int(s.split()[1].split(':')[0])*60+(int(s.split()[1].split(':')[1]))
        hour.append(time)
    data['dayofweek']=dayofweek
    data['hour']=hour
    df = data.drop(['Date/Time'], 1)
    return df

#analyze data
def analyze(time, day):
    master = pd.DataFrame()
    ymaster = pd.DataFrame()
    xmaster = pd.DataFrame()

    master = readadddata('./rides_data.csv')
    master = pd.concat([master, readadddata('./uber-raw-data-apr14.csv')])
    master = pd.concat([master, readadddata('./uber-raw-data-aug14.csv')])
    master = pd.concat([master, readadddata('./uber-raw-data-jul14.csv')])
    master = pd.concat([master, readadddata('./uber-raw-data-jun14.csv')])
    master = pd.concat([master, readadddata('./uber-raw-data-may14.csv')])

    y=master.drop('dayofweek', 1).drop('hour', 1)
    x=master.drop('Lat', 1).drop('Lon', 1)
    xmaster = pd.concat([xmaster, x])
    ymaster = pd.concat([ymaster, y])


    xtimes = xmaster.loc[xmaster['hour']-time <= 5]
    ytimes = ymaster.loc[xmaster['hour']-time <= 5] #gets all rides within 5 minutes
    yrel = ytimes.loc[xtimes['dayofweek'] == day] #gets relevant x's

    minlat = (ymaster['Lat'].values.min())
    minlon = (ymaster['Lon'].values.min())
    maxlat = (ymaster['Lat'].values.max())
    maxlon = (ymaster['Lon'].values.max())

    uniformgrid = []
    latit = minlat
    lonit = minlon
    while lonit <= maxlon:
        while latit<=maxlat:
            zone = []
            zone.append(latit)
            zone.append(lonit)
            latit += .01449 #corresponds to 1 mile, latitude
            zone.append(latit)
            zone.append(lonit+.01455) #corresponds to 1 mile, longitude
            uniformgrid.append(zone)
        lonit += .01455
        latit=minlat

    hotspots = np.zeros((170, 197)) #dimensions of uniformgrid

    for index, row in yrel.iterrows():
        lat = row['Lat']
        lon = row['Lon']
        latbin = int((lat-minlat)/.01449)
        lonbin = int((lon-minlon)/.01455)

        hotspots[latbin][lonbin] += 1


    finalout = []
    for x in hotspots:
        for y in x:
            if y > hotspots.mean() + 5*hotspots.std():
                uWu = []
                uWu.append(y)
                uWu.append(uniformgrid[x.tolist().index(y)*170+hotspots.tolist().index(x.tolist())][0]+random.uniform(0,.01449)/2)
                uWu.append(uniformgrid[x.tolist().index(y)*170+hotspots.tolist().index(x.tolist())][1]+random.uniform(0,.01455)/2)
                finalout.append(uWu)

    export = []
    for oWo in finalout:
        export.append(str(oWo[1]) + "," + str(oWo[2]))
    return export

def getdynamic(export):
    uwu = []
    for owo in export:
        uwu.append('{"lat": ' + owo.split(',')[0] + ', "lng": ' + owo.split(',')[1] + '}')
    return uwu

#to check for cars in a 10-mile radius
def getdistance(lata, longa, latb, longb):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lata)
    lon1 = radians(longa)
    lat2 = radians(latb)
    lon2 = radians(longb)
    dlon = abs(lon2 - lon1)
    dlat = abs(lat2 - lat1)
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance * 0.621371 #convert to miles

def findclosest(mylat, mylon, coords): #coords is a string array
    mindistance = 696969
    index = 0
    c = 0
    for str in coords:
        lat = float(str.split(',')[0])
        lon = float(str.split(',')[1])
        dist = abs(getdistance(lat, lon, mylat, mylon))
        if dist < mindistance:
            mindistance = dist
            index = c
        c += 1
    return coords[index]
