import arcpy

# set the workspace
arcpy.env.workspace = "F:\M.tech\Python\Dissolve & Intersect"

# set the input & output feature class
dis_input = "F:\M.tech\Guwahati_Ward\Guwahati_Ward.shp"
dis_output = "Output_Dis.shp"

# perform a dissolve management
arcpy.Dissolve_management(dis_input, dis_output, "FID")

# set the input & output feature class
input_inter = "Point.shp"
output_inter = "Output_Inter.shp"

# perform an intersect analysis
arcpy.Intersect_analysis([dis_output,input_inter], output_inter)