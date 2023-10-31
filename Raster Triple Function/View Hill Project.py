import arcpy
from arcpy.sa import *
arcpy.env.workspace= "F:\M.tech\Python\Raster Triple Function\View Hill Project"
# Set the input observer point feature class
observer_points = "View.shp"
# Set the input elevation raster
dem = "Dem.tif"
# Set the output viewshed raster
viewshed_raster = "Viewshed.tif"
# Set the analysis properties (e.g. observer height, output coordinate system)
analysis_properties = arcpy.Viewshed_3d(dem, observer_points, viewshed_raster, "#")
# Print the analysis properties to the console
print(analysis_properties)

##Create Hillshade
# Set the input raster and output hillshade path
output_file2 = "Hillshade1.tif"
# Set the Hillshade tool parameters
azimuth = 90
altitude = 45
z_factor = 1
modelShadows = "SHADOWS"
# Execute the Hillshade tool
outHillShade = Hillshade(dem, azimuth, altitude, modelShadows, z_factor)
# Save the output
outHillShade.save(output_file2)
print ("Hillshade Completed")
#Create projection
# Set the input and output paths
output_projected = "Hillshade_Projected.tif"
#Excute the projection tool
Spatial_Reference = arcpy.CreateSpatialReference_management("WGS 1984 UTM Zone 46N")
arcpy.ProjectRaster_management(output_file2,output_projected,Spatial_Reference,"NEAREST","30 30")
print("Task Completed")
