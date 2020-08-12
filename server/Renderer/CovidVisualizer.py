from datetime import datetime
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
matplotlib.use('Agg')


class CovidVisualizer:
    def __init__(self):
        # For storing the rendered images and gif
        self.images_list = []
        self.image_filename_list = []

        # For storing Data retrieved from the dataset
        self.countriesList = []
        self.longitude_coords = []
        self.latitude_coords = []
        self.total_countries = 0
        self.countriesProcessed_ = 0
        self.sorted_dates = []
        self.processed_image_count = 0
        self.currentPath = os.getcwd()

        # Fetching and sorting the data based on Date.
        self.url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
        self.covid19_dataset = pd.read_csv(self.url)

        self.covid19_dataset['Date'] = pd.to_datetime(
            self.covid19_dataset['Date'])
        self.covid19_dataset = self.covid19_dataset.sort_values(
            'Date', ascending=True)
        self.sorted_dates = sorted(list(set(self.covid19_dataset['Date'])))

        self.timeSeriesDataset = self.covid19_dataset
        self.timeSeriesDataset = self.timeSeriesDataset.set_index('Date')

        self.confirmedCases = self.timeSeriesDataset.groupby(
            ['Date']).sum()['Confirmed'].reset_index()

        self.confirmedCases = self.confirmedCases.set_index('Date')

        self.recoveredCases = self.timeSeriesDataset.groupby(
            ['Date']).sum()['Recovered'].reset_index()

        self.recoveredCases = self.recoveredCases.set_index('Date')

        self.deathCases = self.timeSeriesDataset.groupby(
            ['Date']).sum()['Deaths'].reset_index()

        self.deathCases = self.deathCases.set_index('Date')

    def getCountriesList(self):
        # Data Cleaning. Replacing 'Blanks with No_country'
        self.covid19_dataset['Country'] = self.covid19_dataset['Country'].fillna(
            'No_Country')
        self.countries_list = list(set(self.covid19_dataset['Country']))
        print('Total Countries found in Dataset:', len(self.countries_list))
        self.total_countries = len(self.countries_list)

        # prepare a color for each point depending on the continent.
        self.covid19_dataset['labels_enc'] = pd.factorize(
            self.covid19_dataset['Country'])[0]

        return self.countries_list

    # Use of 'OpenStreetMap' API to fetch the Latitude and Longitude information for the Country
    def getCountryCoordinates(self, countryName,
                              output_as='center'):
        url = '{0}{1}{2}'.format('http://nominatim.openstreetmap.org/search?q=',
                                 countryName,
                                 '&format=json&polygon=0')
        response = requests.get(url).json()[0]

        # Fetch the co-ordinates out of the Response received
        if output_as == 'boundingbox':
            lst = response[output_as]
            cordinates = [float(i) for i in lst]
        if output_as == 'center':
            lst = [response.get(key) for key in ['lon', 'lat']]
            cordinates = [float(i) for i in lst]

        return cordinates

    # Append the Longitude and Latitude information into the Data Frame
    def appendCordinatesIntoDataFrame(self, countries):
        self.countriesProcessed_ = 0
        print('Copyrights for Co-ordinates of Countries: OPENSTREETMAP')
        for country in countries:
            if self.countriesProcessed_ % 10 == 0:
                print('Processing Co-ordinates for remaining ' + str(self.total_countries -
                                                                     self.countriesProcessed_) + ' Countries.')
            coordinates = [None, None]
            try:
                coordinates = self.getCountryCoordinates(
                    country, output_as='center')

            except:
                print('Co-ordinates not found for :', country)

            self.longitude_coords.append(coordinates[0])
            self.latitude_coords.append(coordinates[1])

            self.countriesProcessed_ += 1

        latitude_list = []
        longitude_list = []
        for i, r in self.covid19_dataset.iterrows():
            country = r['Country']
            index_list = self.countries_list.index(country)
            latitude_list.append(self.latitude_coords[index_list])
            longitude_list.append(self.longitude_coords[index_list])

        # Adding Co-ordinates back into Data frame
        self.covid19_dataset['Longitude'] = longitude_list
        self.covid19_dataset['Latitude'] = latitude_list
        print('Fetching Co-ordinates for countries completed! \n')

    # Plot the Data on Map
    def getMappedPlot(self, covid_to_plot, date, processed_image_name='', caseType='Confirmed'):
        fig_dimension = 96
        plt.figure(figsize=(2600/fig_dimension, 1800 /
                            fig_dimension), dpi=fig_dimension)

        # Creating the Base Map
        base_map = Basemap(llcrnrlon=-180, llcrnrlat=-65,
                           urcrnrlon=180, urcrnrlat=80)
        base_map.drawmapboundary(fill_color='#B5E3FF', linewidth=0)
        base_map.fillcontinents(color='#737373', alpha=0.3)
        base_map.drawcoastlines(linewidth=0.1, color="#000000")

        total_cases = np.sum(covid_to_plot[caseType])

        # Plot point on World Map
        base_map.scatter(covid_to_plot['Longitude'],
                         covid_to_plot['Latitude'],
                         s=covid_to_plot[caseType] * 4,
                         alpha=0.4,
                         c=covid_to_plot['labels_enc'],
                         cmap="Set1")

        plt.margins(0, 0)
        plt.title(caseType + ' Covid-19 Cases: ' +
                  str(int(total_cases)) + ' [DATED: ' + str(date) + ' ]', fontsize=32)

        plt.text(0.5, 0.5, '[Plot not to scale*]',
                 horizontalalignment='right', verticalalignment='top')

        if processed_image_name != '':
            plt.savefig(processed_image_name, bbox_inches='tight',
                        pad_inches=0)

        # plt.show()

    # Create the Gif using the PNG images created
    def generateGif(self, imageFilenames, gifFilename):
        self.images_list = []
        try:
            for image_name in imageFilenames:
                self.images_list.append(imageio.imread(image_name))
            imageio.mimsave(gifFilename, self.images_list)
            print('Creationg of Gif completed.')
        except:
            print('Error while creating the GIF.')

    # For Each Date Create the respective world heat plot images and then generate the gif of Covid data
    def visualizeData(self, countriesList):
        try:
            for entry in self.sorted_dates:
                if len(countriesList) == 1:
                    covid_record = self.covid19_dataset[self.covid19_dataset['Country']
                                                        == countriesList[0]]
                    print('IF CountryData: ', covid_record.head(10))
                else:
                    covid_record = self.covid19_dataset[self.covid19_dataset['Date'] <= entry]

                covid_record = covid_record[['Country', 'labels_enc', 'Confirmed',
                                             'Deaths', 'Recovered',
                                             'Longitude', 'Latitude']]

                # Aggregates of Mean, Sum and Last Values
                covid_record = covid_record.groupby(['Country', 'labels_enc']).agg({'Confirmed': 'last',
                                                                                    'Deaths': 'last',
                                                                                    'Recovered': 'last',
                                                                                    'Longitude': 'mean',
                                                                                    'Latitude': 'mean'}).reset_index()

                covid_record = covid_record.groupby(['Country', 'labels_enc']).agg({'Confirmed': 'sum',
                                                                                    'Deaths': 'sum',
                                                                                    'Recovered': 'sum',
                                                                                    'Longitude': 'mean',
                                                                                    'Latitude': 'mean'}).reset_index()

                # Plot the Covid Information into PNG image files
                processed_image_name = self.currentPath + '/assets/images/img_' + \
                    str(self.processed_image_count) + '.png'
                self.image_filename_list.append(processed_image_name)
                self.getMappedPlot(covid_record, str(entry)[
                    0:10], processed_image_name)

                self.processed_image_count += 1

            self.generateGif(self.image_filename_list,
                             self.currentPath + '/assets/worldHeatPlot_animation.gif')

            # Create the Gif using the PNG images created
            print('\n Creating gif using non-DEG')
            for image_name in self.image_filename_list:
                self.images_list.append(imageio.imread(image_name))
            imageio.mimsave(
                self.currentPath + '/assets/worldHeatPlot_animation.gif', self.images_list)
            return True
        except:
            print('Failed to Visualize the Data')
            return False

    # Plotting the Time Series
    def plotTimeSeries(self):
        self.image_filename_list = []
        self.processed_image_count = 0

        # gathering min and max values for X axis
        xMinValue = self.confirmedCases.index.min()
        xMaxValue = self.confirmedCases.index.max()

        # gathering the min value for Y axis
        yMinValue = 0
        confirmedCasesMin = self.confirmedCases['Confirmed'].min()
        recoveredCasesMin = self.recoveredCases['Recovered'].min()
        deathsCasesMin = self.deathCases['Deaths'].min()
        yMinValue = max([confirmedCasesMin,
                         recoveredCasesMin, deathsCasesMin])

        # gathering the max value for Y axis
        confirmedCasesMax = self.confirmedCases['Confirmed'].max()
        recoveredCasesMax = self.recoveredCases['Recovered'].max()
        deathsCasesMax = self.deathCases['Deaths'].max()
        yMaxValue = max([confirmedCasesMax, recoveredCasesMax, deathsCasesMax])

        xTextLoc = '2020-03-19'
        yTextLoc = self.confirmedCases['Confirmed'].max()

        print('Initiated Creation of Time Series Plotting.')

        for end in self.sorted_dates:
            endDate = str(end).replace(' 00:00:00', '')
            totalConfirmed = self.confirmedCases.loc[endDate:endDate, 'Confirmed'].max(
            )
            totalRecovered = self.recoveredCases.loc[endDate:endDate, 'Recovered'].max(
            )
            totalDeaths = self.deathCases.loc[endDate:endDate, 'Deaths'].max()

            fig_dimension = 96
            plt.figure(figsize=(2600/fig_dimension, 1800 /
                                fig_dimension), dpi=fig_dimension)

            fig, ax = plt.subplots()

            ax.plot(self.confirmedCases.loc[:endDate, 'Confirmed'], color='blue',
                    linestyle='-', linewidth=0.5, label='Confirmed: ' + str(totalConfirmed))

            ax.plot(self.deathCases.loc[:endDate, 'Deaths'], color='red',
                    markersize=8, linestyle='-', label='Death: ' + str(totalDeaths))

            ax.plot(self.recoveredCases.loc[:endDate, 'Recovered'], color='green',
                    markersize=8, linestyle='-', label='Recovered: ' + str(totalRecovered))

            fig.autofmt_xdate()
            ax.set_xlim([xMinValue,
                         xMaxValue])
            ax.set_ylim([yMinValue, yMaxValue])
            ax.set_ylabel('Covid Cases Count')
            ax.legend()
            plt.title('Covid-19 Time Series Plot ', fontsize=16)

            processed_image_name = self.currentPath + \
                '/assets/images/ts_img_' + \
                str(self.processed_image_count) + '.png'
            self.image_filename_list.append(processed_image_name)
            plt.savefig(processed_image_name,
                        bbox_inches='tight', pad_inches=0.5)
            self.processed_image_count += 1

        self.generateGif(self.image_filename_list, self.currentPath +
                         '/assets/covid_timeSeries_animation.gif')

        print('Time Series Plotting Completed.')
