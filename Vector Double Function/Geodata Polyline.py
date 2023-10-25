import arcpy
import os

# Set workspace environment
arcpy.env.workspace = "F:\M.tech\Python\Geodata and Polyline"

# Create a geodatabase
gdb_name = "My Geodatabase.gdb"
gdb_path = os.path.join(arcpy.env.workspace, gdb_name)
arcpy.CreateFileGDB_management(arcpy.env.workspace, gdb_name)

# Copy polyline shapefile to geodatabase
input_shapefile = "F:\M.tech\Guwahati_Ward\Guwahati_Ward.shp"
output_feature_class = "Polyline"
output_feature_class_path = os.path.join(gdb_path, output_feature_class)
arcpy.CopyFeatures_management(input_shapefile, output_feature_class_path)

