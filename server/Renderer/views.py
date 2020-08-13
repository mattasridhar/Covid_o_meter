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
print('\n\n****** You may now START the Client ******\n\n')
# print('\n\n****** You may now START the Client ******\n\n',
#       json.dumps(covid_visualizer.countryJson))


@api_view(['POST'])
def PostCountryName(req):
    try:
        reqBody = json.loads(req.body.decode('utf-8'))
        return JsonResponse('Country Name is: ' + reqBody.get('Country'), safe=False)
    except ValueError as e:
        print('ERROR: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCountryName(req):
    try:
        # ToDo: Plot and create the GIF using the single Country name
        with open(r'images/worldHeatPlot_animation.gif', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            return HttpResponse(image_data)
    except ValueError as e:
        print('ERROR: ', e.args[0])
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
        print('ERROR: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCovidVisualization(req):
    try:
        if not os.path.exists(r'assets/worldHeatPlot_animation.gif'):
            countriesList = covid_visualizer.getCountriesList()
            covid_visualizer.appendCordinatesIntoDataFrame(countriesList)
            covid_visualizer.visualizeData([])
            print('Plotting Covid-19 Data and Visualizing Completed.')

        if os.path.exists(r'assets/worldHeatPlot_animation.gif'):
            with open(r'assets/worldHeatPlot_animation.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Covid-19 Data Visualizing Available.')
        else:
            with open(r'assets/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                print('Failed to Plot Covid-19 Data and Visualize')

        print('Sending the Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
