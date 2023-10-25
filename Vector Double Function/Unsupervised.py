import arcpy
from arcpy.sa import *

# Set the input raster file
input_raster = "F:\M.tech\SoftSkill\Landsat2022\layerstack.img"

# Set the number of classes for classification
num_classes = 5

# Set the output classified raster file
output_raster = "F:\M.tech\SoftSkill\Unsuper.tif"

# Set the spatial reference (if required)
spatial_reference = arcpy.Describe(input_raster).spatialReference

# Perform unsupervised classification using KMeans algorithm
classified_raster = KMeans(input_raster, num_classes)

# Save the classified raster to output file
classified_raster.save(output_raster)

# Optional: Define the color ramp for visualization
color_ramp = arcpy.sa.CreateUniqueValueRenderer(input_raster)
color_ramp.classField = "Class_Name"  # Set the field name for class names if available
classified_raster.save(output_raster)

# Apply the color ramp to the classified raster
classified_layer = arcpy.MakeRasterLayer_management(output_raster, "classified_layer")[0]
arcpy.mapping.AddLayer(data_frame, classified_layer)
layer = arcpy.mapping.ListLayers(mxd, "classified_layer", data_frame)[0]
layer.symbology = color_ramp

# Refresh the active view (if needed)
arcpy.RefreshActiveView()

# Refresh the table of contents (if needed)
arcpy.RefreshTOC()
