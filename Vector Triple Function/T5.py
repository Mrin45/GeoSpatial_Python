import arcpy
import os

# Set the workspace
# Set workspace environment
arcpy.env.workspace = "F:\M.tech\Python\Vector Triple Function\T5"

# Create a geodatabase
gdb_name = "My Geodatabase.gdb"
gdb_path = os.path.join(arcpy.env.workspace, gdb_name)
arcpy.CreateFileGDB_management(arcpy.env.workspace, gdb_name)


# Convert a feature class to a geodatabase
input_feature_class = "F:\M.tech\Python\Guwahati_Ward\Guwahati_Ward.shp"
output_fc = arcpy.FeatureClassToGeodatabase_conversion(input_feature_class, gdb_path)
print("Feature class converted to geodatabase:", output_fc)

# Copy features to the geodatabase
input_features = "F:\M.tech\Python\Guwahati_Ward\Guwahati_Ward.shp"
output_features = "output_fc_class"
output_feature_class_path = os.path.join(gdb_path, output_features)
arcpy.CopyFeatures_management(input_features, output_feature_class_path)
print("Task Completed")
