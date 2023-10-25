import arcpy

arcpy.env.workspace = "F:\M.tech\Python\Centroid & XY"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
in_feature = "Guwahati_Ward.shp"
out_feature = "Output_Centroid.shp"
centroid = arcpy.FeatureToPoint_management(in_feature,out_feature)

xy = arcpy.AddXY_management("Output_Centroid.shp")
msgcount = centroid.messageCount
msgcount1 = xy.messageCount
print centroid.getMessage(msgcount - 1)
print xy.getMessage(msgcount1 - 1)
