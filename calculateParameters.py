from typing import List

import numpy as np
import pandas as pd
import pygeodesy as gd
import time
import itertools
import datetime
import os
import json
import csv
import datetime


ok=0

actual_sensor_coord = []
actual_launch_coord = []
actual_impact_coord = []
speed_of_sound = []
muzzle_velocity = []
average_velocity = []
time_respective_launch = []
time_stamp_launch = []
flight_time_launch = []
time_respective_impact = []
time_stamp_impact = []
name_sensor = []
name_launch = []
name_impact = []

dist_sensor_launch = []
dist_sensor_impact = []
dist_launch_impact = []

time_launch_sensor = []
time_impact_sensor = []
time_launch_impact = []

main_sensor_obj = []
main_launch_obj = []
main_impact_obj = []
signal_time_obj = []

joker_constant = 0
joker_constant_2 = 0

event_array = []

durations = []
impact_times = []
launch_times = []
tmp_2 = ['Launch Muzzle Blast']
tmp_3 = ['Impact Muzzle Blast']
temp_L = []
temp_I = []
launch_seconds = []
impact_seconds = []
headers = ['Event Class', 'Firing Coordinate', 'Impact Coordinate', 'Firing Time', 'Impact Time']

table_data_launch = []
table_data_impact = []

bearing_sensor_launch = []
bearing_sensor_impact = []
bearing_launch_impact = []

def resetAll():
    global actual_sensor_coord,actual_launch_coord,actual_impact_coord,speed_of_sound,muzzle_velocity,\
    average_velocity,time_respective_launch,time_stamp_launch,flight_time_launch ,time_respective_impact,\
    time_stamp_impact,name_sensor,name_launch,name_impact,dist_sensor_launch,dist_sensor_impact,dist_launch_impact,\
    time_launch_sensor,time_impact_sensor,time_launch_impact,main_sensor_obj,main_launch_obj, main_impact_obj,signal_time_obj,\
    table_data_impact,table_data_launch,bearing_sensor_impact,bearing_launch_impact,bearing_sensor_launch

    actual_sensor_coord.clear()
    actual_launch_coord.clear()
    actual_impact_coord.clear()
    speed_of_sound.clear()
    muzzle_velocity.clear()
    average_velocity.clear()
    time_respective_launch.clear()
    time_stamp_launch.clear()
    flight_time_launch.clear()
    time_respective_impact.clear()
    time_stamp_impact.clear()
    name_sensor.clear()
    name_launch.clear()
    name_impact.clear()
    dist_sensor_launch.clear()
    dist_sensor_impact.clear()
    dist_launch_impact.clear()
    time_launch_sensor.clear()
    time_impact_sensor.clear()
    time_launch_impact.clear()
    main_sensor_obj.clear()
    main_launch_obj.clear()
    main_impact_obj.clear()
    signal_time_obj.clear()
    event_array.clear()
    joker_constant=0
    joker_constant_2=0
    table_data_impact.clear()
    table_data_launch.clear()
    bearing_sensor_launch.clear()
    bearing_launch_impact.clear()
    bearing_sensor_impact.clear()
    durations.clear()

def calculate():
    for i in range(0, len(event_array)):
        distance_event = gd.haversine(event_array[i][1][0], event_array[i][1][1], event_array[i][3][0],
                                      event_array[i][3][1], radius=6371008.77141, wrap=False)
        bearing_event = gd.bearing(event_array[i][1][0], event_array[i][1][1], event_array[i][3][0],
                                      event_array[i][3][1])
        dist_launch_impact.append(distance_event)
        bearing_launch_impact.append(bearing_event)
        print(distance_event)
        if event_array[i][4] == 1:
            launch_time = float(event_array[i][5])
            launch_times.append(launch_time)
            if event_array[i][6] == 1:
                duration_event = float(event_array[i][7])
            else:
                duration_event = float(distance_event) / float(event_array[i][7])
            durations.append(duration_event)
            impact_time = (float(event_array[i][5]) + duration_event)
            impact_times.append(float(impact_time))
        elif event_array[i][4] == 2:
            launch_time = int(event_array[i][5][0]) * 36000 + int(event_array[i][5][1]) * 3600 + int(
                event_array[i][5][3]) * 600 + int(event_array[i][5][4]) * 60 + int(event_array[i][5][6]) * 10 + int(
                event_array[i][5][7])
            launch_times.append(float(launch_time))
            if event_array[i][6] == 1:
                duration_event = float(event_array[i][7])
            else:
                duration_event = float(distance_event) / float(event_array[i][7])
            durations.append(duration_event)
            impact_time = int(event_array[i][5][0]) * 36000 + int(event_array[i][5][1]) * 3600 + int(
                event_array[i][5][3]) * 600 + int(event_array[i][5][4]) * 60 + int(event_array[i][5][6]) * 10 + int(
                event_array[i][5][7]) + float(duration_event)
            impact_times.append(float(impact_time))
        stamp_launch = str(datetime.timedelta(seconds=round(launch_time)))
        stamp_impact = str(datetime.timedelta(seconds=round(impact_time)))

        for j in range(0, len(name_sensor)):
            distance_sensor_launch = gd.haversine(event_array[i][1][0], event_array[i][1][1], actual_sensor_coord[j][0],
                                                  actual_sensor_coord[j][1], radius=6371008.77141, wrap=False)
            bearing_s_l = gd.bearing(event_array[i][1][0], event_array[i][1][1], actual_sensor_coord[j][0],
                                                  actual_sensor_coord[j][1])
            dist_sensor_launch.append(distance_sensor_launch)
            bearing_sensor_launch.append(bearing_s_l)
            duration_reach_launch = float(distance_sensor_launch) / float(event_array[i][-1])
            launch_reach_time = str(datetime.timedelta(seconds=round(float(launch_time) + duration_reach_launch)))
            launch_second = float(launch_time) + duration_reach_launch
            launch_seconds.append(round(launch_second, 2))
            distance_sensor_impact = gd.haversine(event_array[i][3][0], event_array[i][3][1], actual_sensor_coord[j][0],
                                                  actual_sensor_coord[j][1], radius=6371008.77141, wrap=False)
            bearing_s_i = gd.bearing(event_array[i][3][0], event_array[i][3][1], actual_sensor_coord[j][0],
                                                  actual_sensor_coord[j][1])
            dist_sensor_impact.append(distance_sensor_impact)
            bearing_sensor_impact.append(bearing_s_i)
            duration_reach_impact = float(distance_sensor_impact) / float(event_array[i][-1])
            impact_reach_time = str(datetime.timedelta(seconds=round(impact_time + duration_reach_impact)))
            impact_second = round((impact_time + duration_reach_impact), 2)
            impact_seconds.append(impact_second)
            time_launch_sensor.append(launch_reach_time)
            time_impact_sensor.append(impact_reach_time)
            temp_L.append(float(launch_time) + duration_reach_launch)
            temp_I.append(float(impact_time + duration_reach_impact))

        tmp_1 = [event_array[i][1], event_array[i][3], stamp_launch, stamp_impact]
        table_data_launch.append(tmp_2 + tmp_1 + time_launch_sensor + launch_seconds)
        table_data_impact.append(tmp_3 + tmp_1 + time_impact_sensor + impact_seconds)

        temp_L.clear()
        temp_I.clear()
        time_impact_sensor.clear()
        time_launch_sensor.clear()
        launch_seconds.clear()
        impact_seconds.clear()



