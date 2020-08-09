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

# Initialize the Covid Visualizer class
covid_visualizer = CovidVisualizer()


@api_view(['POST'])
def PostCountryName(req):
    try:
        print('SRI in POST: ', req.body.decode('utf-8'))
        reqBody = json.loads(req.body.decode('utf-8'))
        return JsonResponse('Country Name is: ' + reqBody.get('Country'), safe=False)
    except ValueError as e:
        print('ERROR: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def GetCountryName(req):
#     try:
#         print('SRI in GET: ', req.method)
#         resp = Response('Country Name is: IND')
#         resp['Access-Control-Allow-Origin'] = '*'
#         return resp
#     except ValueError as e:
#         print('ERROR: ', e.args[0])
#         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCountryName(req):
    try:
        with open(r'images/covid_animation.gif', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            print('SRI in GET_IMG: ', image_data)
            return HttpResponse(image_data)
    except ValueError as e:
        print('ERROR: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetCountriesList(req):
    try:
        print('Accumulating List of Countries')
        countriesList = covid_visualizer.getCountriesList()
        # covid_visualizer.appendCordinatesIntoDataFrame(countriesList)
        # covid_visualizer.visualizeData([])
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
        countriesList = covid_visualizer.getCountriesList()
        covid_visualizer.appendCordinatesIntoDataFrame(countriesList)

        if covid_visualizer.visualizeData([]):
            with open(r'images/covid_animation.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                # , image_data)
                print('Plotting Covid-19 Data and Visualizing Completed.')
        else:
            with open(r'images/failed_to_visualize.gif', "rb") as image_file:
                image_data = base64.b64encode(
                    image_file.read()).decode('utf-8')
                # , image_data)
                print('Failed to Plot Covid-19 Data and Visualize')

        print('Sending the Visualization to Client')
        return HttpResponse(image_data)

    except ValueError as e:
        print('ERROR: ', e.args[0])
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
