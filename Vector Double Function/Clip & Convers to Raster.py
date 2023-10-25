import arcpy

# Set up the arcpy environment
arcpy.env.workspace = "F:\M.tech\Python\Clip & Convers to Raster"

# Input & Output polygon feature class and clip feature class
input_poly = "IND_adm1.shp"
input_clip = "Assam.shp"
output_clip_poly = "output_clip.shp"

# Perform clip operation
arcpy.Clip_analysis(input_poly, input_clip, output_clip_poly)

# Output clipped polygon feature class and raster
output_raster = "output_raster.tif"

# Convert clipped polygon to raster
arcpy.PolygonToRaster_conversion(output_clip_poly, "FID", output_raster)



# Clean up intermediate data from in-memory workspace
#arcpy.Delete_management("F:\M.tech\Python\Clip & Convers to Raster\output_.shp")


