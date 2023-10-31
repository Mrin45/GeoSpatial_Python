import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.workspace = "F:\M.tech\Python\Raster Triple Function\Unsup Smooth Clip"

input_layer1 = "Composite.tif"
output_layer1 = "Unsupervised.tif"
unsup = IsoClusterUnsupervisedClassification(input_layer1,7,50,20,"#")
unsup.save(output_layer1)
print("Unsupervised Classification completed successfully!")

#Smoothing
input_layer2 = output_layer1
output_layer2 = "Smoothing.tif"
neighbour = NbrCircle(3,"CELL")
op_focal = FocalStatistics (input_layer2,neighbour,"MAJORITY","")
op_focal.save(output_layer2)
mc = arcpy.GetMessageCount()
print arcpy.GetMessage(mc-1)
print("Smoothing completed")

#Clipping
input_layer3 = input_layer2
clip_feature = "F:\M.tech\Python\Guwahati_Ward\Guwahati_Ward.shp"
output_layer3 = "Smoothing_Clip.tif"
arcpy.Clip_management(input_layer3,"#", output_layer3,clip_feature,"#", "clippingGeometry")
print("Clipping Completed")
