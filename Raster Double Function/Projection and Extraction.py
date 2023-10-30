# To set projection of DEM
import arcpy
#Set the workspace environment
arcpy.env.workspace = "F:\M.tech\Python\Raster Double Function\Projection and Extraction"
# Set the input and output paths
input_dam = "Raster_Clipped.tif"
output_projected = "Projected_Dem.tif"
#Excute the projection tool
Spatial_Reference = arcpy.CreateSpatialReference_management("WGS 1984 UTM Zone 46N")
arcpy.ProjectRaster_management(input_dam,output_projected,Spatial_Reference,"NEAREST","30 30")
print("Task Completed")
