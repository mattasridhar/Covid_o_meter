from matplotlib.ticker import FuncFormatter, MaxNLocator
import shutil
import pycountry
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from pygifsicle import optimize
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
        self.datesProcessed_ = 0
        self.sorted_dates = []
        self.processed_image_count = 0
        self.currentPath = os.getcwd()

        # For sending to client all the Countries and its codes
        self.countryJson = {}

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

        self.radialDataset = self.covid19_dataset
        self.radialDataset = self.radialDataset.set_index('Date')

        # Checking and creating folder structure for saving plots
        self.imagesDir = self.currentPath + '/assets/images'
        self.animationDir = self.currentPath + '/assets/animation'
        if not os.path.exists(self.imagesDir):
            os.mkdir(self.imagesDir)
            print('Images Directory created.')
        if not os.path.exists(self.animationDir):
            os.mkdir(self.animationDir)
            print('Animation Directory created.')

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
                         s=covid_to_plot[caseType],
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
            optimize(gifFilename)  # optimize and reduce the gif size
            print('Creation of Gif completed.')
            print('Clearing the /images directory')
            shutil.rmtree(self.imagesDir)
            os.mkdir(self.imagesDir)
        except:
            print('Error while creating the GIF.')

    # For Each Date Create the respective world heat plot images and then generate the gif of Covid data
    def visualizeData(self, countriesList):
        try:
            print('Initiated Creation of World Heat Map Plot')
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
                processed_image_name = self.imagesDir + '/img_' + \
                    str(self.processed_image_count) + '.png'
                self.image_filename_list.append(processed_image_name)
                self.getMappedPlot(covid_record, str(entry)[
                    0:10], processed_image_name)

                self.processed_image_count += 1

            self.generateGif(self.image_filename_list,
                             self.animationDir + '/worldHeatPlot_animation.gif')

            print('World Heat Map Plotting Completed')
            return True
        except:
            print('Failed to Visualize the Data')
            return False

    # Plotting the Time Series
    def plotTimeSeries(self):
        # Reset Counters
        self.image_filename_list = []
        self.processed_image_count = 0

        # Gather requied Data
        confirmedCases = self.timeSeriesDataset.groupby(
            ['Date']).sum()['Confirmed'].reset_index()
        confirmedCases = confirmedCases.set_index('Date')

        recoveredCases = self.timeSeriesDataset.groupby(
            ['Date']).sum()['Recovered'].reset_index()
        recoveredCases = recoveredCases.set_index('Date')

        deathCases = self.timeSeriesDataset.groupby(
            ['Date']).sum()['Deaths'].reset_index()
        deathCases = deathCases.set_index('Date')

        # gathering min and max values for X axis
        xMinValue = confirmedCases.index.min()
        xMaxValue = confirmedCases.index.max()

        # gathering the min value for Y axis
        yMinValue = 0
        confirmedCasesMin = confirmedCases['Confirmed'].min()
        recoveredCasesMin = recoveredCases['Recovered'].min()
        deathsCasesMin = deathCases['Deaths'].min()
        yMinValue = max([confirmedCasesMin,
                         recoveredCasesMin, deathsCasesMin])

        # gathering the max value for Y axis
        confirmedCasesMax = confirmedCases['Confirmed'].max()
        recoveredCasesMax = recoveredCases['Recovered'].max()
        deathsCasesMax = deathCases['Deaths'].max()
        yMaxValue = max([confirmedCasesMax, recoveredCasesMax, deathsCasesMax])

        print('Initiated Creation of Time Series Plot.')

        for end in self.sorted_dates:
            endDate = str(end).replace(' 00:00:00', '')
            totalConfirmed = confirmedCases.loc[endDate:endDate, 'Confirmed'].max(
            )
            totalRecovered = recoveredCases.loc[endDate:endDate, 'Recovered'].max(
            )
            totalDeaths = deathCases.loc[endDate:endDate, 'Deaths'].max()

            fig_dimension = 96
            plt.figure(figsize=(2600/fig_dimension, 1800 /
                                fig_dimension), dpi=fig_dimension)

            fig, ax = plt.subplots()

            ax.plot(confirmedCases.loc[:endDate, 'Confirmed'], color='blue',
                    linestyle='-', linewidth=0.5, label='Confirmed: ' + str(totalConfirmed))

            ax.plot(deathCases.loc[:endDate, 'Deaths'], color='red',
                    markersize=8, linestyle='-', label='Death: ' + str(totalDeaths))

            ax.plot(recoveredCases.loc[:endDate, 'Recovered'], color='green',
                    markersize=8, linestyle='-', label='Recovered: ' + str(totalRecovered))

            fig.autofmt_xdate()
            ax.set_xlim([xMinValue,
                         xMaxValue])
            ax.set_ylim([yMinValue, yMaxValue])
            ax.set_ylabel('Covid Cases Count')
            ax.legend()
            plt.title('Covid-19 Time Series Plot ', fontsize=16)

            processed_image_name = self.imagesDir + '/ts_img_' + \
                str(self.processed_image_count) + '.png'
            self.image_filename_list.append(processed_image_name)
            plt.savefig(processed_image_name,
                        bbox_inches='tight', pad_inches=0.5)
            self.processed_image_count += 1

        self.generateGif(self.image_filename_list,
                         self.animationDir + '/covid_timeSeries_animation.gif')

        print('Time Series Plotting Completed.')

    # Iterate through the countries list and create a Radial plot gif for each country
    def generateRadialChart(self, countriesList):
        print('Initiated Creation of Radial Chart Plot.')
        for countryName in countriesList:
            self.image_filename_list = []
            country_record = self.radialDataset.loc[self.radialDataset['Country'] == countryName]
            country_confirmed = country_record[[
                'Confirmed', 'Recovered', 'Deaths']]

            self.plotRadialChart(country_confirmed, countryName)

            gifFilename = self.animationDir + \
                '/covid_radialChart_animation_' + countryName + '.gif'
            self.generateGif(self.image_filename_list, gifFilename)

            print('Gif creation for ' + countryName + ' completed.')

        print('RadialChart Plotting Completed.')

    # Create the Radial Plot and save the images
    def plotRadialChart(self, df, countryName):
        self.processed_image_count = 0
        confirmedMax = df['Confirmed'].max()
        recoveredMax = df['Recovered'].max()
        deathsMax = df['Deaths'].max()
        for date in self.sorted_dates:
            endDate = str(date).replace(' 00:00:00', '')
            plt = self.createRings(
                df.loc[endDate:endDate, 'Confirmed'], confirmedMax, df.loc[endDate:endDate, 'Recovered'], recoveredMax, df.loc[endDate:endDate, 'Deaths'], deathsMax, countryName, endDate)
            self.processed_image_count += 1
            processed_image_name = self.imagesDir + '/rc_img_' + \
                str(self.processed_image_count) + '.png'
            self.image_filename_list.append(processed_image_name)
            plt.savefig(processed_image_name,
                        bbox_inches='tight', pad_inches=0.5)

    # Plot and form the Radial charts and return the plotted object
    def createRings(self, confirmed_df_value, confirmedMax, recovered_df_value, recoveredMax, deaths_df_value, deathsMax, countryName, endDate):
        # Creating Labels, PieSizes and Color gradient for the Pie plotting
        confirmedLabels = ['Confirmed: ' +
                           str(confirmed_df_value.max()), '']
        recoveredLabels = ['Recovered: ' + str(recovered_df_value.max()), '']
        deathsLabels = ['Deaths: ' + str(deaths_df_value.max()), '']

        maxPieValue = max([confirmedMax, recoveredMax, deathsMax])
        confirmedPieSizes = [confirmed_df_value,
                             (maxPieValue-confirmed_df_value)]
        recoveredPieSizes = [recovered_df_value,
                             (maxPieValue-recovered_df_value)]
        deathPieSizes = [deaths_df_value, (maxPieValue-deaths_df_value)]

        confirmColor, recoverColor, deathColor = [
            plt.cm.Blues, plt.cm.Greens, plt.cm.Reds]

        fig_dimension = 96
        plt.figure(figsize=(2600/fig_dimension, 1800 /
                            fig_dimension), dpi=fig_dimension)
        fig, ax = plt.subplots()
        ax.axis('equal')

        # Confirmed Ring Plot
        confirmedPie, _ = ax.pie(confirmedPieSizes, radius=1.3,
                                 labels=confirmedLabels, colors=[confirmColor(0.8), confirmColor(0.2)], textprops={'fontsize': 0, 'color': 'white'})
        plt.setp(confirmedPie, width=0.3, edgecolor='white')

        # Recovered Ring Plot
        recoveredPie, _ = ax.pie(recoveredPieSizes, radius=1.3-0.3, labels=recoveredLabels,
                                 labeldistance=0.7, colors=[recoverColor(0.8), recoverColor(0.2)], textprops={'fontsize': 0, 'color': 'white'})
        plt.setp(recoveredPie, width=0.4, edgecolor='white')

        # Death Ring Plot
        deathsPie, _ = ax.pie(deathPieSizes, radius=1-0.3, labels=deathsLabels,
                              labeldistance=0.7, colors=[deathColor(0.8), deathColor(0.2)], textprops={'fontsize': 0, 'color': 'white'})
        plt.setp(deathsPie, width=0.2, edgecolor='white')

        ax.legend(loc='upper right', bbox_to_anchor=(0.75, 0.5, 0.5, 0.5))
        plt.title(
            'Covid-19 Radial Chart Plot - ' + countryName + '\n [ Date: ' + endDate + ' ]\n', fontsize=16)
        plt.margins(0, 0)

        return plt

    # Convert the Date into Integer
    def getTransformedDate(self, date):
        transformedDate = 19
        onlyDate = str(date).replace(' 00:00:00', '')
        noHyphes = str(onlyDate).replace('-', '')
        noYear = str(noHyphes).replace('2020', '')
        transformedDate = int(noHyphes)
        return transformedDate

    # Append the Country codes and Date9converted to numeric) information into the Data Frame
    def append3DCodesIntoDataFrame(self, countries):
        self.countriesProcessed_ = 0
        self.datesProcessed_ = 0
        countryCodes = []
        alphaCodes = []
        transformedDate = []

        # Returns the Numeric value of each country
        numericMapping = {
            country.name: country.numeric for country in pycountry.countries}
        alphaMapping = {
            country.name: country.alpha_2 for country in pycountry.countries}

        for country in countries:
            if self.countriesProcessed_ % 50 == 0:
                print('Processing Country Codes for remaining ' +
                      str(self.total_countries - self.countriesProcessed_) + ' Countries.')

            codecInfo = numericMapping.get(country)
            alphaInfo = alphaMapping.get(country)
            self.countryJson[country] = alphaInfo
            if codecInfo == None:
                codecInfo = 0

            countryCodes.append(int(codecInfo))
            alphaCodes.append(alphaInfo)

            self.countriesProcessed_ += 1

        # Setting Day count since the start of Covid
        for date in self.sorted_dates:
            self.datesProcessed_ += 1
            transformedDateInfo = self.datesProcessed_
            transformedDate.append(transformedDateInfo)

        countryCode_list = []
        countryAlphaCode_list = []
        transformedDate_list = []
        for i, r in self.covid19_dataset.iterrows():
            country = r['Country']
            index_list = self.countries_list.index(country)
            countryCode_list.append(countryCodes[index_list])
            countryAlphaCode_list.append(alphaCodes[index_list])
            transformedDate_list.append(transformedDate[index_list])

        # Adding Co-ordinates back into Data frame
        self.covid19_dataset['CountryCode'] = countryCode_list
        self.covid19_dataset['CountryAlphaCode'] = countryAlphaCode_list
        self.covid19_dataset['TransformedDate'] = transformedDate_list
        print('Appending additional information required for 3D Heat map for countries completed! \n')

    # 3D plot for each category across all countries
    def generate3DHeatMap(self, countriesList):
        self.append3DCodesIntoDataFrame(countriesList)
        self.heat3DDataset = self.covid19_dataset
        self.heat3DDataset = self.heat3DDataset.set_index('Date')
        # self.heat3DDataset = self.heat3DDataset.set_index('CountryCode')

        self.processed_image_count = 0
        self.image_filename_list = []

        # Gather min&max for each axis
        confirmMin = self.heat3DDataset['Confirmed'].min()
        confirmMax = self.heat3DDataset['Confirmed'].max()

        # Removing all entries without country codes
        self.heat3DDataset = self.heat3DDataset[self.heat3DDataset.CountryCode != 0]

        for date in self.sorted_dates:
            endDate = str(date).replace(' 00:00:00', '')

            plt = self.create3DHeatMap(
                self.heat3DDataset.loc[endDate:endDate], countriesList, confirmMin, confirmMax)
            plt.title(
                'Covid-19 3D Heat Map Plot \n [ Date: ' + endDate + ' ]\n', fontsize=16)

            self.processed_image_count += 1
            processed_image_name = self.imagesDir + '/hm_img_' + \
                str(self.processed_image_count) + '.png'
            self.image_filename_list.append(processed_image_name)
            plt.savefig(processed_image_name,
                        bbox_inches='tight', pad_inches=0.5)

        gifFilename = self.animationDir + \
            '/covid_3dHeatMap_animation.gif'
        self.generateGif(self.image_filename_list, gifFilename)

        print('3D HeatMap Plotting Completed.')

    # plot the heat map for each date
    def create3DHeatMap(self, df, countriesList, confirmMin, confirmMax):
        fig_dimension = 196

        xlabelMap = {}
        ylabelMap = {}
        countryLabel = []
        countryCodeList = []
        transDtList = []

        for i, r in df.iterrows():
            countryCode = r['CountryCode']
            countryAlpha = r['CountryAlphaCode']
            countryName = r['Country']
            xlabelMap[countryCode] = countryAlpha
            countryLabel.append(countryAlpha)
            countryCodeList.append(countryCode)
            txDt = r['TransformedDate']
            ylabelMap[i] = txDt
            transDtList.append(txDt)

        fig, ax = plt.subplots()
        ax.axis('equal')

        # Setting this dimension makes the GIF more clear but file-size is too large
        # fig = plt.figure(figsize=(2600/fig_dimension, 1800 /fig_dimension), dpi=fig_dimension)

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot_trisurf(df['TransformedDate'], df['CountryCode'],
                        df['Confirmed'], cmap=plt.cm.jet, linewidth=0.2, edgecolor='none')

        ax.axes.set_zlim3d(confirmMin, confirmMax)

        ax.set_xlabel('Country Codes', fontsize=12, labelpad=8)
        ax.set_ylabel('# of Covid-19 Days', fontsize=12, labelpad=8)
        ax.set_zlabel('\tConfirmed Cases', fontsize=12, labelpad=8)

        surf = ax.plot_trisurf(df['TransformedDate'], df['CountryCode'],
                               df['Confirmed'], cmap=plt.cm.jet, linewidth=0.2)
        cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
        cbar.set_label('Confirmed cases: ' +
                       str(df['Confirmed'].max()), fontsize=12)

        # Uncomment if you want to label the X and Y axes but they fluctute a lot so commented them out to save Memory at transfer
        """ def xformat_fn(tick_val, tick_pos):
            try:
                if int(tick_val) in countryCodeList:
                    return countryLabel[int(tick_val)]
                else:
                    return str(tick_val).replace('.0', '')
            except:
                return xlabelMap[int(tick_val)].replace('.0', '')
        ax.xaxis.set_major_formatter(FuncFormatter(xformat_fn))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        def yformat_fn(tick_val, tick_pos):
            try:
                if int(tick_val) in transDtList:
                    return transDtList[int(tick_val)]
                else:
                    return str(tick_val).replace('.0', '')
            except:
                return ylabelMap[int(tick_val)].replace('.0', '')
        ax.yaxis.set_major_formatter(FuncFormatter(yformat_fn))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True)) """

        ax.view_init(25, 55)

        return plt

    # Plot the 3 cases for all dates across different Countries
    def generateStackedArea(self, countriesList):
        self.append3DCodesIntoDataFrame(countriesList)
        self.processed_image_count = 0
        self.image_filename_list = []
        self.stackedDataset = self.covid19_dataset
        self.stackedDataset = self.stackedDataset.set_index('Date')

        # Removing all entries without country codes
        self.stackedDataset = self.stackedDataset[self.stackedDataset.CountryCode != 0]

        # Gather min&max for each axis
        confirmMin = self.stackedDataset['Confirmed'].min()
        confirmMax = self.stackedDataset['Confirmed'].max()

        ccMin = self.stackedDataset['CountryCode'].min()
        ccMax = self.stackedDataset['CountryCode'].max()

        for date in self.sorted_dates:
            endDate = str(date).replace(' 00:00:00', '')
            covid_record = self.stackedDataset.loc[endDate:endDate]
            covid_record = covid_record[['Country', 'CountryAlphaCode', 'Confirmed',
                                         'Deaths', 'Recovered',
                                         'CountryCode', 'TransformedDate']]
            plt = self.createStackMap(
                covid_record, endDate, confirmMin, confirmMax, ccMin, ccMax)

            self.processed_image_count += 1
            processed_image_name = self.imagesDir + '/sa_img_' + \
                str(self.processed_image_count) + '.png'
            self.image_filename_list.append(processed_image_name)
            plt.savefig(processed_image_name,
                        bbox_inches='tight', pad_inches=0.5)

        gifFilename = self.animationDir + \
            '/covid_StackMap_animation.gif'
        self.generateGif(self.image_filename_list, gifFilename)

        print('Stack Map Plotting Completed.')

    def createStackMap(self, covid_record, endDate, confirmMin, confirmMax, ccMin, ccMax):
        countryCodeList = []
        countryLabel = []
        confirmedList = []
        recoveredList = []
        deathsList = []
        labelMap = {}

        for i, r in covid_record.iterrows():
            countryCode = r['CountryCode']
            countryAlpha = r['CountryAlphaCode']
            confirmed = r['Confirmed']
            recovered = r['Recovered']
            deaths = r['Deaths']
            countryName = r['Country']
            labelMap[countryCode] = countryAlpha
            countryCodeList.append(countryCode)
            countryLabel.append(countryAlpha)
            confirmedList.append(confirmed)
            recoveredList.append(recovered)
            deathsList.append(deaths)

        # fig.autofmt_xdate()
        fig, ax = plt.subplots()

        x = countryCodeList
        y = [confirmedList, recoveredList, deathsList]
        covidCases = {
            'Confirmed': confirmedList,
            'Recovered': recoveredList,
            'Deaths': deathsList
        }

        pal = ["#237DFC", "#44FC23", "#FF6054"]
        ax.stackplot(x, covidCases.values(),
                     labels=covidCases.keys(), colors=pal)
        ax.legend(loc='upper right')
        ax.set_title('Covid-19 Stacked Plot \n [ Date: ' + str(endDate) + ' ]')
        ax.set_xlabel('Country')
        ax.set_ylabel('# of Covid cases')
        ax.set_xlim([ccMin, ccMax])
        ax.set_ylim([confirmMin, confirmMax])

        def format_fn(tick_val, tick_pos):
            try:
                if int(tick_val) in x:
                    return countryLabel[int(tick_val)]
                else:
                    return str(tick_val).replace('.0', '')
            except:
                return labelMap[int(tick_val)].replace('.0', '')
        ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        return plt
