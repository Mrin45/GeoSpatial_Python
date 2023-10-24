import arcpy

# set the workspace
arcpy.env.workspace = "F:\M.tech\Python\Centroid"

# set the input feature class
input = "F:\M.tech\Guwahati_Ward\Guwahati_Ward.shp"
# set the output feature class
output = "Centroid.shp"

# perform the centroid
arcpy.FeatureToPoint_management(input, output, "CENTROID")