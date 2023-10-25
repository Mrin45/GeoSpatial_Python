import arcpy

# Set up the arcpy environment
arcpy.env.workspace = "F:\M.tech\Python\Intersect & MultiBuffer"

# Set the input and output paths
input_file1 = "Assam.shp"
input_intersect = "Guwahati_Ward.shp"
output_file1 = "intersect.shp"

# Execute the intersect tool
arcpy.Intersect_analysis([input_file1,input_intersect],output_file1)
# Set the input and output paths

output_file2 = "Multiple_Buffer.shp"
# Execute the Buffer tool
arcpy.MultipleRingBuffer_analysis(output_file1, output_file2, [1, 2, 3],"Kilometers", "", "ALL")
