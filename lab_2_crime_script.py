## Nate Butler 6/21/19 GEOG 682 Lab 2

## Load shape files in QGIS: points and ploygons
zip_uri = '/vsizip/C:/Users/nbutler4/Downloads/Crime_Incidents_in_2017.zip'
shp =  QgsVectorLayer(zip_uri, 'Crime_Incidents_in_2017.zip', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp)

zip_uri = '/vsizip/C:/Users/nbutler4/Downloads/Police_Districts.zip'
shp =  QgsVectorLayer(zip_uri, 'Police_Districts.zip', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp) 

## Join Polygons by location
import processing  
processing.runalg("qgis:joinattributesbylocation",{
"TARGET":"C:/Temp/Police_Districts.shp", 
"JOIN":"C:/Temp/Crime_Incidents_in_2017.shp", 
"PREDICATE":u'contains',   
"SUMMARY":0,
"KEEP":1,
"OUTPUT":"C:/Temp/crime_districts.shp"})

## Load final outpout layer to QGIS
zip_uri = '/vsizip/C:/Temp/crime_districts.zip'
shp =  QgsVectorLayer(zip_uri, 'crime_districts.zip', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp) 

## Which police district had the most crimes 2017? How many crimes occurred there? 
# Anwser: District three crime count-5895









