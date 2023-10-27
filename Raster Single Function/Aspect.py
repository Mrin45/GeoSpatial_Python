# Create Aspect from DEM
import arcpy
#Set the worksapce environment
arcpy.env.workspace= "F:\M.tech\Python\Raster Single Function\Aspect"
#Set input and output paths
input_dem =  "Raster_Clipped.tif"
output_Aspect= "Aspect.tif"
#Excute the Aspect tool
arcpy.Aspect_3d(input_dem,output_Aspect)
print("Task Completed")
