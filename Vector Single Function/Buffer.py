import arcpy

# set the workspace
arcpy.env.workspace = "F:\M.tech\Python\Buffer"

# set the input feature class
input_fc = "Export_Output.shp"

# set the output feature class
output_fc = "Buffer_Output\Buff_Output.shp"

# set the buffer distance in meters
buffer_distance = "1000 meters"

# perform the buffer
arcpy.Buffer_analysis(input_fc, output_fc, buffer_distance)