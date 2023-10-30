#To perform Contour from DEM
import arcpy
from arcpy import env
from arcpy.sa import *
# Set the workspace environment
arcpy.env.workspace = "F:\M.tech\Python\Raster Double Function\Contour and Hillshade"
# Set the input and output paths
input_file1 = "Raster_Clipped.tif"
output_file1 = "Contour.shp"
contour_interval = 50
base_contour = 0
# Execute the contour tool
arcpy.Contour_3d(input_file1,output_file1,contour_interval,base_contour)
print("Contour Completed")
#Create Hillshade
# Set the input raster and output hillshade path
input_file2 = "Projected_Dem.tif"
output_file2 = "Hillshade.tif"
# Set the Hillshade tool parameters
azimuth = 90
altitude = 45
z_factor = 1
modelShadows = "SHADOWS"
# Execute the Hillshade tool
outHillShade = Hillshade(input_file2, azimuth, altitude, modelShadows, z_factor)
# Save the output
outHillShade.save(output_file2)
print ( "Hillshade Completed")
