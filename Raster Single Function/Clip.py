#Clip a raster file
import arcpy
# Set the workspace environment
arcpy.env.workspace = "F:\M.tech\Python\Raster Single Function\Clip"
# Set the input and output paths
input_raster = "N26_e091_1arc_v3.tif"
clip_features = "Guwahati_Ward.shp"
output_raster = "Raster_Clipped.tif"
# Execute the Clip tool
arcpy.Clip_management(input_raster,"#", output_raster,clip_features,"#", "clippingGeometry")
print("Task Completed")
