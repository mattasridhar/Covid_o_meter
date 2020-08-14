"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Renderer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countryName/', views.PostCountryName),
    path('api/hello/', views.GetCountryName),
    path('api/countriesList/', views.GetCountriesList),
    path('api/countriesJson/', views.GetCountriesJSON),
    path('api/visualize/worldheatmap/', views.GetCovidWorldVisualization),
    path('api/visualize/timeseries/', views.GetCovidTimeSeriesVisualization),
    path('api/visualize/radialchart/', views.GetCovidRadialChartVisualization),
    path('api/visualize/heatmap/', views.GetCovid3dHeatMapVisualization),
    path('api/visualize/stackedmap/', views.GetCovidStackedAreaVisualization),
    path('api/visualize/scattermap/', views.GetCovid3dScatterMapVisualization),
]
