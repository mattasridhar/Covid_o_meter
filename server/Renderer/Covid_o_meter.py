# Covid-O-Meter is a python code which provides real time Covid data visualizations in graphical format

"""
Created on Sat Aug  1 15:11:37 2020

@author: Matta Sridhar
"""

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import datetime
import time
import requests
from time import sleep

import imageio
from IPython.display import Image
from mpl_toolkits.basemap import Basemap

import os
os.environ['PROJ_LIB'] = 'opt/anaconda3/lib/python3.8/site-packages/mpl_toolkits/basemap'

images_list = []
image_filename_list = []

url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
covid19_dataset = pd.read_csv(url)
covid19_dataset['Date'] = pd.to_datetime(covid19_dataset['Date'])
covid19_dataset = covid19_dataset.sort_values('Date', ascending=True)

covid19_dataset['Country'] = covid19_dataset['Country'].fillna('No_Country')

# Total Countries
countries_list = list(set(covid19_dataset['Country']))
print('Unique Countries found:', str(len(countries_list)))

# get the co-ordinates of countries using openstreetmap API


def getCountryCoordinates(countryName,
                          output_as='center'):
    url = '{0}{1}{2}'.format('http://nominatim.openstreetmap.org/search?q=',
                             countryName,
                             '&format=json&polygon=0')
    response = requests.get(url).json()[0]

    # parse response to list
    if output_as == 'boundingbox':
        lst = response[output_as]
        output = [float(i) for i in lst]
    if output_as == 'center':
        lst = [response.get(key) for key in ['lon', 'lat']]
        output = [float(i) for i in lst]

    return output


longitude_coords = []
latitude_coords = []
total_countries = len(countries_list)
countriesProcessed_ = 0
for country in countries_list:
    if countriesProcessed_ % 10 == 0:
        print(total_countries - countriesProcessed_)
    time.sleep(0.2)
    coordinates = [None, None]
    try:
        coordinates = getCountryCoordinates(country, output_as='center')

    except:
        print('Co-ordinates not found for :', country)

    longitude_coords.append(coordinates[0])
    latitude_coords.append(coordinates[1])

    countriesProcessed_ += 1

# Add geos back to data frame
latitude_list = []
longitude_list = []
for i, r in covid19_dataset.iterrows():
    country = r['Country']
    index_list = countries_list.index(country)
    latitude_list.append(latitude_coords[index_list])
    longitude_list.append(longitude_coords[index_list])

# add to data frame
covid19_dataset['Longitude'] = longitude_list
covid19_dataset['Latitude'] = latitude_list
# print('data head: \n', covid19_dataset.head(10))

covid19_dataset[covid19_dataset['Country'] == 'Ireland']


def getMappedPlot(covid_to_plot, date, processed_image_name=''):
    # Set the dimension of the figure
    plt.figure(figsize=(16, 8))
    # Set the dimension of the figure
    fig_dimension = 96
    plt.figure(figsize=(2600/fig_dimension, 1800 /
                        fig_dimension), dpi=fig_dimension)

    # Make the background map
    base_map = Basemap(llcrnrlon=-180, llcrnrlat=-65,
                       urcrnrlon=180, urcrnrlat=80)
    base_map.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
    base_map.fillcontinents(color='grey', alpha=0.3)
    base_map.drawcoastlines(linewidth=0.1, color="white")

    total_confirmed = np.sum(covid_to_plot['Confirmed'])

    # Add a point per position
    base_map.scatter(covid_to_plot['Longitude'],
                     covid_to_plot['Latitude'],
                     # play around with the size or use np.log if you dont like the big circles
                     s=covid_to_plot['Confirmed'] * 8,
                     alpha=0.4,
                     c=covid_to_plot['labels_enc'],
                     cmap="Set1")

    plt.title(str(date) + ' Confirmed Covid-19 Cases: ' +
              str(int(total_confirmed)) + '\n(circles not to scale)', fontsize=50)

    if processed_image_name != '':
        plt.savefig(processed_image_name)

    # plt.show()


# Create color map
# prepare a color for each point depending on the continent.
covid19_dataset['labels_enc'] = pd.factorize(covid19_dataset['Country'])[0]
covid19_dataset['labels_enc']


# build time lapse with accumulator count by country
sorted_dates = sorted(list(set(covid19_dataset['Date'])))
# print('Dates Sorted: \n', sorted_dates)

processed_image_count = 0
for entry in sorted_dates:
    covid_record = covid19_dataset[covid19_dataset['Date'] <= entry]

    # simplify data set
    covid_record = covid_record[['Country', 'labels_enc', 'Confirmed',
                                 'Deaths', 'Recovered',
                                           'Longitude', 'Latitude']]

    # get totals by province then by country as these are cumulative values by province first then by country and not all countries have provinces

    # group by country and sum/mean values
    covid_record = covid_record.groupby(['Country', 'labels_enc']).agg({'Confirmed': 'last',
                                                                        'Deaths': 'last',
                                                                                  'Recovered': 'last',
                                                                                  'Longitude': 'mean',
                                                                                  'Latitude': 'mean'}).reset_index()

    # group by country and sum/mean values
    covid_record = covid_record.groupby(['Country', 'labels_enc']).agg({'Confirmed': 'sum',
                                                                        'Deaths': 'sum',
                                                                                  'Recovered': 'sum',
                                                                                  'Longitude': 'mean',
                                                                                  'Latitude': 'mean'}).reset_index()

    # map out confirmed cases
    processed_image_name = 'server/images/img_' + \
        str(processed_image_count) + '.png'
    image_filename_list.append(processed_image_name)
    getMappedPlot(covid_record, str(entry)[0:10], processed_image_name)

    processed_image_count += 1

for image_name in image_filename_list:
    images_list.append(imageio.imread(image_name))
imageio.mimsave('server/covid_animation.gif', images_list)

print("SRIDHAR")
