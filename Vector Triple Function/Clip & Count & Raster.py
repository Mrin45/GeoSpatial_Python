# Set up the arcpy environment
import arcpy.management

arcpy.env.workspace = "F:\M.tech\Python\Vector Triple Function\T1"

# Input & Output polygon feature class and clip feature class
input_poly = "IND_adm2.shp"
input_clip = "Assam_district.shp"
output_poly = "output_clip.shp"

# Perform clip operation
arcpy.Clip_analysis(input_poly, input_clip, output_poly)
#perform count
input_feature2 = output_poly
count = arcpy.GetCount_management(input_feature2)
print(count)

# Output clipped polygon feature class and raster
output_raster = "output_raster.tif"
# Convert clipped polygon to raster
arcpy.PolygonToRaster_conversion(output_poly, "FID", output_raster)