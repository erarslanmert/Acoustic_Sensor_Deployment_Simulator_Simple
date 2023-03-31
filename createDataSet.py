import numpy as np
import pandas as pd
import pygeodesy as gd
import itertools
import datetime
import os
import csv
import json
import time

manual_sensor_coord = [51.983189,5.900222]
manual_launch_coord = [51.987209,5.933490]
manual_impact_coord = [51.991025,5.866114]
manual_muzzle_velocity = 1000 #m/s

number_of_shots = 1

speed_of_sound = 330 #m/s

bearing_launch = gd.bearing(manual_sensor_coord[0], manual_sensor_coord[1], manual_launch_coord[0], manual_launch_coord[1])
bearing_impact = gd.bearing(manual_sensor_coord[0], manual_sensor_coord[1], manual_impact_coord[0], manual_impact_coord[1])
distance_launch = gd.haversine(manual_sensor_coord[0], manual_sensor_coord[1], manual_launch_coord[0], manual_launch_coord[1],radius=6371008.77141, wrap=False)
distance_impact = gd.haversine(manual_sensor_coord[0], manual_sensor_coord[1], manual_impact_coord[0], manual_impact_coord[1],radius=6371008.77141, wrap=False)


