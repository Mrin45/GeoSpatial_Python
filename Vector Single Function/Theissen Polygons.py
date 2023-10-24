import arcpy

# Set up the input and output paths
input_points = "Export_Output.shp"
output_polygons = "Output_Polygons.shp"

# Set the environment settings
arcpy.env.workspace = "F:\M.tech\Python\Theissen Polygons"
arcpy.env.overwriteOutput = True
fields_to_copy = "ALL"

# Use the CreateThiessenPolygons_management tool to generate Thiessen polygons
arcpy.CreateThiessenPolygons_analysis(input_points, output_polygons, fields_to_copy)


