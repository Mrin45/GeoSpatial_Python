import arcpy
import numpy as np
from sklearn.cluster import KMeans

# Set the input raster file
input_raster = "F:\M.tech\SoftSkill\Landsat2022\layerstack.img"

# Set the number of classes for classification
num_classes = 5

# Set the output classified raster file
output_raster = "F:\M.tech\SoftSkill\Unsuper.tif"

# Read the input raster as a numpy array
raster_array = arcpy.RasterToNumPyArray(input_raster)

# Reshape the array to 2D for clustering
rows, cols, bands = raster_array.shape
reshaped_array = np.reshape(raster_array, (rows * cols, bands))

# Perform unsupervised classification using K-means algorithm
kmeans = KMeans(n_clusters=num_classes, random_state=0)
kmeans.fit(reshaped_array)

# Get the cluster labels for each pixel
labels = kmeans.predict(reshaped_array)

# Reshape the labels back to 2D
classified_array = np.reshape(labels, (rows, cols))

# Create a new raster from the classified array
classified_raster = arcpy.NumPyArrayToRaster(classified_array, arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                             arcpy.env.cellSize, arcpy.env.cellSize)

# Save the classified raster to output file
classified_raster.save(output_raster)

# Optional: Define the color ramp for visualization
color_ramp = arcpy.sa.CreateUniqueValueRenderer(output_raster)
color_ramp.classField = "Value"  # Set the field name for class values

# Apply the color ramp to the classified raster
classified_layer = arcpy.MakeRasterLayer_management(output_raster, "classified_layer")[0]

# Specify the name of your map data frame
data_frame_name = "layerstack.img"

# Add the classified layer to the map data frame
mxd = arcpy.mapping.MapDocument("CURRENT")
data_frame = arcpy.mapping.ListDataFrames(mxd, data_frame_name)[0]
arcpy.mapping.AddLayer(data_frame, classified_layer)
layer = arcpy.mapping.ListLayers(mxd, "classified_layer", data_frame)[0]
layer.symbology = color_ramp

# Refresh the active view (if needed)
arcpy.RefreshActiveView()

# Refresh the table of contents (if needed)
arcpy.RefreshTOC()

