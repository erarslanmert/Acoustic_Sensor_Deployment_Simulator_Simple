import pandas as pd
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
from folium.plugins import TimestampedGeoJson
from folium.plugins import MousePosition, MeasureControl,MiniMap
import time
from selenium import webdriver
import os
import json
import calculateParameters as Cp


url_temp = " "
geo_path = ('TL_SCCO_CTPRVN.json')
kr_geo_data = json.load(open(geo_path, encoding='utf-8'))
def prepare_df_date(df):
    df['Time'] = pd.to_datetime(df['Time'])
    return df

def create_geojson_features(df_con,fill_color_confirmed='#FC766AFF',
                           weight=1,fill_opacity=0.1):
    print('> Creating GeoJSON features...')

    features = []
    feature = []
    for _, row in df_con.iterrows():
        radius = row['Radius']
        opacity = row['Opacity']
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['Longitude'],row['Latitude']]
            },
            'properties': {
                'time': row['Time'].__str__(),
                'style': {'color': row['Color']},
                'icon': 'circle',
                'iconstyle': {
                    'fillColor': row['Color'],
                    'fillOpacity': opacity,
                    'stroke': 'true',
                    'radius': radius,
                    'weight': weight,

                }
            }
        }
        features.append(feature)


    print('> finishing GeoJSON features...')
    return features


def main_refresh():
    global url_temp
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    driver.get(r"C:\Users\Eraslan\PycharmProjects\mdtProject1\Sensor.html")
    time.sleep(0.5)
    driver.refresh()
    time.sleep(0.5)
    url_temp = driver.current_url
    driver.close()


def press_it(layout):
    mainmap = folium.Map(location=(Cp.actual_sensor_coord[0][0], Cp.actual_sensor_coord[0][1]), control_scale=True,
                         tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                         attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=13,zoom_control=False,
                         detect_retina=True, min_zoom=13,max_zoom=13)
    mainmap.add_child(MiniMap())
    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)
    mainmap.add_child(MeasureControl())
    for i in Cp.actual_sensor_coord:
        folium.Marker(location=i, icon=folium.features.CustomIcon('icon_sensor.png', icon_size=(21, 24)),
                      popup=(Cp.name_sensor[Cp.actual_sensor_coord.index(i)])).add_to(mainmap)
    for j in Cp.actual_launch_coord:
        folium.Marker(location=j, icon=folium.features.CustomIcon('icon_artillery.png', icon_size=(20, 13)),
                      popup=(Cp.name_launch[Cp.actual_launch_coord.index(j)])).add_to(mainmap)
    for k in Cp.actual_impact_coord:
        folium.Marker(location=k, icon=folium.features.CustomIcon('impact_point.png', icon_size=(20, 14)),
                      popup=(Cp.name_impact[Cp.actual_impact_coord.index(k)])).add_to(mainmap)
    df_con = pd.read_csv('animate.csv')
    df_con = prepare_df_date(df_con)
    features = create_geojson_features(df_con, fill_opacity=0.3, weight=1)

    TimestampedGeoJson(
        {'type': 'FeatureCollection',
         'features': features}
        , period='PT1S'
        , duration='PT1S'
        , add_last_point=True
        , auto_play=False
        , loop=False
        , max_speed=10
        , loop_button=True
        , date_options='mm:ss'
        , time_slider_drag_update=True
        , transition_time=10
    ).add_to(mainmap)

    mainmap.save(os.path.join('Sensor.html'))

    view = QWebEngineView()
    main_refresh()
    view.setUrl(QUrl(url_temp))
    view.setContentsMargins(2, 5, 28, 50)
    view.setFixedSize(1205, 781)
    layout.addWidget(view)

