
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import numpy as np
import pandas as pd
import pygeodesy as gd
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWebEngineWidgets, QtWidgets
import folium, io, sys
from folium.plugins import  TimestampedGeoJson
from folium.plugins import Draw, MousePosition, MeasureControl,MiniMap
import time
from selenium import webdriver
import itertools
import datetime
import os
import csv
import json
from threading import Thread



lat = 0
lon = 0
lat_1, lon_1 = (51.983225, 5.900198)
lat_2, lon_2 = (51.987186, 5.933464)

lat_firing, lon_firing = (51.987186, 5.933464)

speed_of_sound = 330
bearing = 0
distance = 0
ToA = 0
temp_coordinates = []
temp_cumulative = []
cumulative_coordinates = []
time_of_arrivals = []
cumulative_ToA = []
last_list = []
last_list_float = []

speed_of_sound = 330
bearing = 0
distance = 0
ToA = 0
time_of_arrivals = []

url_temp = " "
geo_path = (r'C:\Users\Eraslan\PycharmProjects\mdtProject1\Data\Si-Do/TL_SCCO_CTPRVN.json')
kr_geo_data = json.load(open(geo_path, encoding='utf-8'))


def prepare_df_date(df):
    # turning date field into timestamps
    df['Date'] = pd.to_datetime(df['Date'])
    # geocoding does not know about 'Mainland China', so lets fix it into an API acceptable form
#     df.loc[df['Country/Region'] == 'Mainland China', 'Country/Region'] = 'China'
    # also geocoding does not like deal with NAs
    df['Confirmed'] = df['Confirmed'].fillna(0)
    return df


def create_geojson_features(df_con,df_on,radius_max=2000,radius_min=2,fill_color_confirmed='#FC766AFF',
                            fill_color_recovered='#0A5E2AFF',
                            fill_color_death='#E80018',weight=1,fill_opacity=0.5):
    print('> Creating GeoJSON features...')

    features = []
    feature = []
    # df_con
    for _, row in df_con.iterrows():
        radius = np.sqrt(row['Confirmed'])
        if radius != 0:
            if radius < radius_min:
                radius = radius_min

            if radius > radius_max:
                radius = radius_max



            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [row['Lon1'], row['Lat1']]
                },
                'properties': {
                    'time': row['Date'].__str__(),
                    'style': {'color': fill_color_confirmed},
                    'icon': 'circle',
                    'iconstyle': {
                        'fillColor': fill_color_confirmed,
                        'fillOpacity': fill_opacity,
                        'stroke': 'true',
                        'radius': radius,
                        'weight': weight,

                    }
                }
            }
        features.append(feature)

    for _, row in df_on.iterrows():
        radius = np.sqrt(row['Confirmed'])
        if radius != 0:
            if radius < radius_min:
                radius = radius_min

            if radius > radius_max:
                radius = radius_max

        size = radius, radius
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['Lon1'], row['Lat1']]
            },
            'properties': {
                'time': row['Date'].__str__(),
                'style': {'color': fill_color_confirmed},
                'icon': 'marker',
                'iconstyle': {
                    'iconUrl': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAANCAYAAACpUE5eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAEzSURBVDhPYwzMLPzPpGbIwMDEzEAJ+P/6McP/dy8ZGJPaJv2XCkhiYGRlhUqRBz5ePMHw5dYlBiZGJiYGZjY2BmZWyjATCwsDyCwmqAVYwZ+fPxje3r/N8OjMETD+9e0Lw/9//6Cy2AFeA7++e8Nw9/AuhtOLpoPxh6ePGP7++Q2VxQ7wGnh+1TyGM8tmMlzduhKMj0zrYPjy6jlUFjvAayAbJxcDMzMLw7+/f8GYjZsbGE74UwNeA2WMrRhUnXwY1F38wFjF3pOBg5cPKosd4DVQWt+UQcM9gEE3IBqMlW1cGNh4KDCQmYWVQUrHiEHHOxSMWYFBwMjICJXFDvAaCAcgQwgYBAOMGQ0d/9m1zYBGU5b1/jx/yPD37XMGxuzqxv+/hKSIdgEuwPztIwPzjy8MAPCUXZfok3RYAAAAAElFTkSuQmCC',
                    'iconSize': 25,
                    'fillOpacity': 0.1

                    }
            }
        }
        features.append(feature)

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['Lon'], row['Lat']]
            },
            'properties': {
                'time': row['Date'].__str__(),
                'style': {'color': fill_color_confirmed},
                'icon': 'marker',
                'iconstyle': {
                    'iconUrl': 'http://pngimg.com/uploads/explosion/explosion_PNG15344.png',
                    'iconSize': 25,
                    'fillOpacity': 0.1

                }
            }
        }
        features.append(feature)

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['Lon2'], row['Lat2']]
            },
            'properties': {
                'time': row['Date'].__str__(),
                'style': {'color': fill_color_confirmed},
                'icon': 'marker',
                'iconstyle': {
                    'iconUrl': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAANCAYAAACpUE5eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAEzSURBVDhPYwzMLPzPpGbIwMDEzEAJ+P/6McP/dy8ZGJPaJv2XCkhiYGRlhUqRBz5ePMHw5dYlBiZGJiYGZjY2BmZWyjATCwsDyCwmqAVYwZ+fPxje3r/N8OjMETD+9e0Lw/9//6Cy2AFeA7++e8Nw9/AuhtOLpoPxh6ePGP7++Q2VxQ7wGnh+1TyGM8tmMlzduhKMj0zrYPjy6jlUFjvAayAbJxcDMzMLw7+/f8GYjZsbGE74UwNeA2WMrRhUnXwY1F38wFjF3pOBg5cPKosd4DVQWt+UQcM9gEE3IBqMlW1cGNh4KDCQmYWVQUrHiEHHOxSMWYFBwMjICJXFDvAaCAcgQwgYBAOMGQ0d/9m1zYBGU5b1/jx/yPD37XMGxuzqxv+/hKSIdgEuwPztIwPzjy8MAPCUXZfok3RYAAAAAElFTkSuQmCC',
                    'iconSize': 25,
                    'fillOpacity': 0.1

                }
            }
        }
        features.append(feature)

    print('> finishing GeoJSON features...')
    return features


def showAcousticProperties(coordinates):
    global bearing, distance, bearing, ToA, speed_of_sound, time_of_arrivals
    global cumulative_coordinates, cumulative_ToA, temp_cumulative, temp_coordinates, last_list, lat, lon

    bearing_launch = gd.bearing(coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1])
    bearing_impact = gd.bearing(coordinates[2][0],coordinates[2][1],coordinates[1][0],coordinates[1][1])
    distance_launch = gd.haversine(coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1], radius=6371008.77141, wrap=False)
    distance_impact = gd.haversine(coordinates[2][0],coordinates[2][1],coordinates[1][0], coordinates[1][1],radius=6371008.77141, wrap=False)

    print("bearing from launch: ", (bearing_launch))
    print("bearing from impact: ", (bearing_impact))
    print("distance to launch: ", (distance_launch))
    print("distance to impact: ", (distance_impact))

    ToA_launch = distance_launch / speed_of_sound
    ToA_impact = distance_impact / speed_of_sound

    print("time of arrival from launch: ", ToA_launch)
    print("time of arrival from impact: ", ToA_impact)
    print("-------------------------------------------------------------------------------------------------------------")

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        global last_list
        coords_dict = json.loads(msg)
        lon = coords_dict['geometry']['coordinates'][0]
        lat = coords_dict['geometry']['coordinates'][1]
        temp_coordinates.append(lat)
        temp_coordinates.append(lon)
        temp_cumulative.append(temp_coordinates)
        cumulative_coordinates.append(str(temp_cumulative[-1]))

        j = 0
        for i in cumulative_coordinates:
            a = cumulative_coordinates[j].split(', ')
            a[0] = float(a[0].replace('[', ''))
            a[-1] = float(a[-1].replace(']', ''))
            last_list_float.append(a)
            j = j + 1

        last_list_float.sort()
        last_list = list(last_list_float for last_list_float, _ in itertools.groupby(last_list_float))
        temp_coordinates.pop(-1)
        temp_coordinates.pop(0)

def main_refresh():
    global url_temp
    # open URL in browser

    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    driver.get("C:\\Users\\Eraslan\\PycharmProjects\\mdtProject1\\Sensor.html")

    #define loop to refresh page 3 times
    time.sleep(0.5)
    driver.refresh()
    time.sleep(0.5)

    url_temp = driver.current_url

    driver.close()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.label.move(10,10)

    def initWindow(self):
        self.setWindowTitle(self.tr("MAP PROJECT"))
        self.setFixedSize(1600, 900)
        self.buttonUI()

    def buttonUI(self):
        shortPathButton = QtWidgets.QPushButton(self.tr("Find shortest path"))
        button2 = QtWidgets.QPushButton(self.tr("Another path"))
        button3 = QtWidgets.QPushButton(self.tr("Another path"))

        shortPathButton.setFixedSize(200, 50)
        button2.setFixedSize(200, 50)
        button3.setFixedSize(200, 50)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setContentsMargins(50, 50, 50, 50)
        self.view.setFixedSize(1200,800)


        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QHBoxLayout(central_widget)


        button_container = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout(button_container)
        vlay.setSpacing(20)
        vlay.addStretch()
        vlay.addWidget(shortPathButton)
        vlay.addWidget(button2)
        vlay.addWidget(button3)
        vlay.addStretch()

        lay.addWidget(button_container)
        lay.addWidget(self.view, stretch=1)


        m = folium.Map(location=(51.983225, 5.900198), control_scale=True, tiles="Stamen Terrain", zoom_start=9,
                       detect_retina=True)

        m.add_child(MeasureControl())
        m.add_child(MiniMap())

        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri', name='Esri Satellite', overlay=False, control=True).add_to(m)

        folium.LayerControl().add_to(m)

        draw = Draw(
            draw_options={'polyline': False, 'rectangle': False, 'polygon': False, 'circle': False,
                          'marker.icon_sensor': True, 'circlemarker': True},
            edit_options={'edit': True})
        m.add_child(draw)

        formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
        MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                      prefix="Coordinates:",
                      lat_formatter=formatter, lng_formatter=formatter, ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())