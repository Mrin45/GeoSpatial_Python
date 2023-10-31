 #To perform Contour from DEM
import arcpy
# Set the workspace environment
arcpy.env.workspace = "F:\M.tech\Python\Raster Triple Function\Contour Slope Aspect"
# Set the input and output paths
input_dem = "Raster_Clipped.tif"
output_contour = "Contour.shp"
contour_interval = 50
base_contour = 0
# Execute the contour tool
arcpy.Contour_3d(input_dem,output_contour,contour_interval,base_contour)
print("Aspect Completed")

# Create slope from DEM
input_dem =  "Projected_Dem.tif"
output_Slope= "Slope.tif"

arcpy.Slope_3d(input_dem,output_Slope,"DEGREE", "1")
print("Slope Completed")

# Create Aspect from DEM

#Set input and output paths
output_Aspect= "Aspect.tif"
#Excute the Aspect tool
arcpy.Aspect_3d(input_dem,output_Aspect)
print("Aspect Completed")
