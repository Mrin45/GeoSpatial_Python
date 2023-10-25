# Description: Intersecting two feature
import arcpy
# Set the workspace environment
arcpy.env.workspace = "F:\PYTHON"
# Set the input feature classes
input_feature1 = "ShapeFile\India_DisputedBoundary.shp"
input_feature2 = "ShapeFile\J&K_OldMap.shp"
# Set the output feature class
output_feature1 = "Results\intersect.shp"
# Perform the intersection
arcpy.Intersect_analysis([input_feature1,input_feature2],output_feature1)
print("Intersection Completed")
#Centeroid:
#Set input and output paths
input_file = "Results\intersect.shp"
output_file = "Results\Centriod.shp"
#Excute the Aspect tool
arcpy.FeatureToPoint_management(input_file,output_file,"CENTROID")
print("Centriod Completed")
#Buffer
input_feature4 = "Results\intersect.shp"
output_feature3 = "Results\JK_Buffer.shp"
buffer_value = "5000 Meters"
arcpy.Buffer_analysis(input_feature4, output_feature3,buffer_value)
print("Bufffer Completed")
