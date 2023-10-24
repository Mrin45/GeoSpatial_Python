import arcpy

# set the workspace
arcpy.env.workspace = "F:\M.tech\Python\Dissolve"

# set the input feature class
input_fc = "F:\M.tech\Guwahati_Ward\Guwahati_Ward.shp"

# set the output feature class
output_fc = "DisOutput.shp"

# set the dissolve field
dissolve_field = ["FID"]

# perform the dissolve
arcpy.Dissolve_management(input_fc, output_fc,dissolve_field)