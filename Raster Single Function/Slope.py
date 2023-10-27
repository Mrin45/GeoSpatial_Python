# Create slope from DEM
import arcpy
#Set the worksapce environment
arcpy.env.workspace= "F:\M.tech\Python\Raster Single Function\Slope"
#Set input and output paths
input_dem =  "Raster_Clipped.tif"
output_Slope= "Slope.tif"
#Excute the slope tool
arcpy.Slope_3d(input_dem,output_Slope,"DEGREE", "1")
print("Task Completed")
