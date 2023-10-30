import arcpy
arcpy.env.workspace= "F:\M.tech\Python\Raster Double Function\Band Comp and Clip"
# Perform band composition
arcpy.CompositeBands_management(["Blue.TIF","Green.TIF","Red.TIF","NIR.TIF"], "Composite.tif")
# Print a message indicating that the composition was successful
print("Band composition completed successfully!")

#Clip a raster file
# Set the input and output paths
clip_features = "F:\M.tech\Python\Guwahati_Ward\Guwahati_Ward.shp"
output_raster = "Composite_Clipped.tif"
# Execute the Clip tool
arcpy.Clip_management("Composite.tif","#", output_raster,clip_features,"#", "clippingGeometry")
print("Task Completed")
