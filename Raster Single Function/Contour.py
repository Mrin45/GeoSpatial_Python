#To perform Contour from DEM
import arcpy
# Set the workspace environment
arcpy.env.workspace = "F:\M.tech\Python\Raster Single Function\Contour"
# Set the input and output paths
input_dem = "Raster_Clipped.tif"
output_contour = "Contour.shp"
contour_interval = 50
base_contour = 0
# Execute the contour tool
arcpy.Contour_3d(input_dem,output_contour,contour_interval,base_contour)
print("Task Completed")
