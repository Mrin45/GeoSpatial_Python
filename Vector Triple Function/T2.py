#Erase Function
import arcpy
# set up workspace
arcpy.env.workspace = "F:\PYTHON\ShapeFile"
# set up input and output file paths
input_file = "Admin2.shp"
erase_file = "Tripura.shp"
output_file = "erase1.shp"
# perform erase analysis
arcpy.Erase_analysis(input_file,erase_file,output_file)
#Union Function
# set up input and output file paths
input_file1 = output_file
input_file2 = erase_file
output_file2 = "india_union1.shp"
#perform Union Analysis
arcpy.Union_analysis([input_file1,input_file2],output_file2)
print("Task Completed")
# Description: Create a buffer of 5000m on boundary
# Set the input and output feature classes
input_feature = "Tripura.shp"
output_feature = "Tripura_Buffer.shp"
# Set the buffer distance
buffer_value = "5000 Meters"
# Create the buffer
arcpy.Buffer_analysis(input_feature, output_feature, buffer_value)
print("Task Completed")
