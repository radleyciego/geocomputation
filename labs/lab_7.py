import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT") # create a reference to project
map = aprx.listMaps()[0] # create a reference to map within project
map.addDataFromPath("C:/Users/r_ciego/Downloads/Building_Footprints/geo_export_58aa0107-1d7c-4812-9468-d3f50ad766bb.shp") # import builfing footprint shapefile

arcpy.management.SelectLayerByAttribute(
    "geo_export_58aa0107-1d7c-4812-9468-d3f50ad766bb",
    "NEW_SELECTION",
    '"heightroof" > 50'
) # select features that fulfill heightroof condition of 50 units or greater
arcpy.management.CopyFeatures("geo_export_58aa0107-1d7c-4812-9468-d3f50ad766bb", "height_roof_50") # copy selected features into new height_roof_50 layer