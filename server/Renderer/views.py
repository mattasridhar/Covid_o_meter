import json
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
import base64
from Renderer.CovidVisualizer import CovidVisualizer
import os.path
import json

# Initialize the Covid Visualizer class
covid_visualizer = CovidVisualizer()
countriesList = covid_visualizer.getCountriesList()
covid_visualizer.appendCordinatesIntoDataFrame(countriesList)
covid_visualizer.visualizeData([])
covid_visualizer.plotTimeSeries()
covid_visualizer.generateRadialChart(['China', 'India', 'Ireland'])
covid_visualizer.generate3DHeatMap(countriesList)
covid_visualizer.generateStackedArea(countriesList)
covid_visualizer.generate3DScatterMap()
countriesJson = covid_visualizer.countryJson
print('\n\n****** You may now START the Client ******\n\n')


@api_view(['POST'])
def PostCountryName(req):
    try:
        reqBody = json.loads(req.body.decode('utf-8'))
        return JsonResponse('Country Name is: ' + reqBody.get('Country'), safe=False)
    except ValueError as e:
        print('ERROR in PostCountryName: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCountryName(req):
    try:
        # ToDo: Plot and create the GIF using the single Country name
        with open(r'images/worldHeatPlot_animation.gif', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            return HttpResponse(image_data)
    except ValueError as e:
        print('ERROR in GetCountryName: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCountriesList(req):
    try:
        print('Accumulating List of Countries')
        countriesList = covid_visualizer.getCountriesList()

        resp = Response(countriesList)
        resp['Content-Type'] = 'text/csv'
        print('Sending the List of Countries')
        return resp
    except ValueError as e:
        print('ERROR in GetCountriesList: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCountriesJSON(req):
    try:
        print('Accumulating JSON of Countries')
        if len(countriesJson.keys()) == 0:
            countriesList = covid_visualizer.getCountriesList()
            covid_visualizer.append3DCodesIntoDataFrame(countriesList)
            countriesJsonStr = json.dumps(covid_visualizer.countryJson)
        else:
            countriesJsonStr = json.dumps(countriesJson)

        resp = Response(countriesJsonStr)
        resp['Content-Type'] = 'application/json'
        print('Sending the Countries and Country Code JSON')
        return resp
    except ValueError as e:
        print('ERROR in GetCountriesJSON: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCovidWorldVisualization(req):
    try:
        if not os.path.exists(r'assets/animation/worldHeatPlot_animation.gif'):
            countriesList = covid_visualizer.getCountriesList()
            covid_visualizer.appendCordinatesIntoDataFrame(countriesList)
            covid_visualizer.visualizeData([])
            print('Plotting Covid-19 Data for World Heat Map Visualizing Completed.')

        if os.path.exists(r'assets/animation/worldHeatPlot_animation.gif'):
            with open(r'assets/animation/worldHeatPlot_animation.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Covid-19 World Heat Map Visualizing Available.')
        else:
            with open(r'assets/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Failed to Plot Covid-19 World Heat Map')

        print('Sending the World Heat Map Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR in getCovidWorldVisualization: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCovidTimeSeriesVisualization(req):
    try:
        if not os.path.exists(r'assets/animation/covid_timeSeries_animation.gif'):
            covid_visualizer.plotTimeSeries()
            print('Plotting Covid-19 Data for Time Series and Visualizing Completed.')

        if os.path.exists(r'assets/animation/covid_timeSeries_animation.gif'):
            with open(r'assets/animation/covid_timeSeries_animation.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Covid-19 Time Series Visualizing Available.')
        else:
            with open(r'assets/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Failed to Plot Covid-19 Time Series')

        print('Sending the Time Series Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR in GetCovidTimeSeriesVisualization: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCovidRadialChartVisualization(req):
    try:
        if not os.path.exists(r'assets/animation/covid_radialChart_animation_India.gif'):
            countriesList = covid_visualizer.getCountriesList()
            covid_visualizer.generateRadialChart(['China', 'India', 'Ireland'])
            print('Plotting Covid-19 Data for Radial Chart and Visualizing Completed.')

        if os.path.exists(r'assets/animation/covid_radialChart_animation_India.gif'):
            with open(r'assets/animation/covid_radialChart_animation_India.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Covid-19 Radial Chart Visualizing Available.')
        else:
            with open(r'assets/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Failed to Plot Covid-19 Radial Chart')

        print('Sending the Radial Chart Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR in GetCovidRadialChartVisualization: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCovid3dHeatMapVisualization(req):
    try:
        if not os.path.exists(r'assets/animation/covid_3dHeatMap_animation.gif'):
            countriesList = covid_visualizer.getCountriesList()
            covid_visualizer.generate3DHeatMap(countriesList)
            print('Plotting Covid-19 Data for 3D Heat Map and Visualizing Completed.')

        if os.path.exists(r'assets/animation/covid_3dHeatMap_animation.gif'):
            with open(r'assets/animation/covid_3dHeatMap_animation.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Covid-19 3D Heat Map Visualizing Available.')
        else:
            with open(r'assets/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Failed to Plot Covid-19 3D Heat Map')

        print('Sending the 3D Heat Map Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR in GetCovid3dHeatMapVisualization: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCovidStackedAreaVisualization(req):
    try:
        if not os.path.exists(r'assets/animation/covid_StackMap_animation.gif'):
            countriesList = covid_visualizer.getCountriesList()
            covid_visualizer.generateStackedArea(countriesList)
            print(
                'Plotting Covid-19 Data for Stacked Area Map and Visualizing Completed.')

        if os.path.exists(r'assets/animation/covid_StackMap_animation.gif'):
            with open(r'assets/animation/covid_StackMap_animation.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Covid-19 Stacked Area Map Visualizing Available.')
        else:
            with open(r'assets/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Failed to Plot Covid-19 Stacked Area Map')

        print('Sending the Stacked Area Map Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR in GetCovidStackedAreaVisualization: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCovid3dScatterMapVisualization(req):
    try:
        if not os.path.exists(r'assets/animation/covid_3dScatterMap_animation.gif'):
            covid_visualizer.generate3DScatterMap()
            print('Plotting Covid-19 Data for 3D Scatter Map and Visualizing Completed.')

        if os.path.exists(r'assets/animation/covid_3dScatterMap_animation.gif'):
            with open(r'assets/animation/covid_3dScatterMap_animation.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Covid-19 3D Scatter Map Visualizing Available.')
        else:
            with open(r'assets/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Failed to Plot Covid-19 Stacked Area Map')

        print('Sending the 3D Scatter Map Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR in GetCovid3dScatterMapVisualization: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
