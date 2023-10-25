import arcpy
arcpy.env.workspace = "E:\PYTHON"
inp = "ShapeFile\Schools1.shp"
out = "Results\School_Mean.shp"
arcpy.MeanCenter_stats(inp, out)
out = "Results\School_Median.shp"
arcpy.MedianCenter_stats(inp, out)
out = "Results\Thiessen_schools.shp"
outFields = "ALL"
arcpy.CreateThiessenPolygons_analysis(inp,out,outFields)
