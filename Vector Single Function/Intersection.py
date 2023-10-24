import arcpy

# set the workspace
arcpy.env.workspace = "F:\M.tech\Python\Intersection"

# set the input feature classes
input_fc1 = "F:\M.tech\Guwahati_Ward\Guwahati_Ward.shp"
input_fc2 = "Point.shp"
# set the output feature class
output_fc = "IntersectionOutput\OutputInter.shp"

# perform the intersection
arcpy.Intersect_analysis([input_fc1, input_fc2], output_fc)
