import arcpy

# Set the input and clip features
in_features = "F:\M.tech\Python\Road Shp file\New_Shapefile.shp"
clip_features = "F:\M.tech\Python\Guwahati_Ward\Guwahati_Ward.shp"

# Set the output feature class
out_feature_class = "F:\M.tech\Python\clip output\output.shp"

# Clip the features
arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
