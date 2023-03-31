import numpy as np
import pandas as pd
import pygeodesy as gd
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWebEngineWidgets
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



class Window(QWidget):
    def __init__(self):
        global last_list
        global url_temp
        super(Window, self).__init__()
        self.setWindowTitle('MDT')
        self.setMinimumSize(1600, 900)

        layout = QGridLayout()

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

        webView = QWebEngineView()
        page = WebEnginePage(webView)
        webView.setPage(page)
        webView.setHtml(data.getvalue().decode())
        webView.setFixedSize(600, 600)
        layout.addWidget(webView, 0, 0)
        my_button = QPushButton("Animate the scenario",
                                clicked=lambda: press_it())
        layout.addWidget(my_button)
        self.setLayout(layout)


        def press_it():
            if len(last_list) < 3:
                print("Please mark in order: \n 1) Launch Point \n 2) Sensor Post \n 3) Impact Point")
            else:
                with open('Sensor.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Lat', 'Lon', 'Lat1', 'Lon1', 'Lat2', 'Lon2', 'Confirmed', 'Date'])
                    date = []
                    for i in range(0, 10000):
                        date.append(str(datetime.timedelta(seconds=i)))
                        writer.writerow(
                            [last_list[0][0], last_list[0][1], last_list[1][0], last_list[1][1], last_list[2][0],
                             last_list[2][1], i, date[i]])

                print(
                    "\n---------------------------------------------------------------------------------------------------")
                print("coordinates : ", last_list)
                print("Number of Elements", len(last_list))
                showAcousticProperties(last_list)

                m2 = folium.Map(location=(last_list[0][0], last_list[0][1]), control_scale=True, zoom_start=9,
                                detect_retina=True)

                m2.add_child(MeasureControl())

                folium.TileLayer(
                    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    attr='Esri', name='Esri Satellite', overlay=False, control=True).add_to(m2)

                df_con = pd.read_csv(r'C:\Users\Eraslan\PycharmProjects\mdtProject1/Sensor.csv')
                df_con = prepare_df_date(df_con)
                features = create_geojson_features(df_con, fill_opacity=0.3, weight=1)

                TimestampedGeoJson(
                    {'type': 'FeatureCollection',
                     'features': features}
                    , period='PT1M'
                    , duration='PT1M'
                    , add_last_point=True
                    , auto_play=False
                    , loop=False
                    , max_speed=1
                    , loop_button=True
                    , date_options='hh:mm:ss'
                    , time_slider_drag_update=True
                    , transition_time=10
                ).add_to(m2)

                m2.save(os.path.join('Sensor.html'))

                webView2 = QWebEngineView()
                main_refresh()
                webView2.setUrl(QUrl(url_temp))
                webView2.setFixedSize(600, 600)
                layout.addWidget(webView2, 0, 0)


if __name__ == '__main__':
    app = QApplication([sys.argv])
    app.setStyleSheet('''QWidget {font-size: 35px;} ''')

    myApp = Window()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
