import csv
import datetime

sensors = ['S1','S2','S3']
launchs = ['L1','L2']
impacts = ['I1','I2']
distances = [20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170]
date=[]


with open('mission.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(sensors)
    for i in sensors:
        writer.writerow(distances)
