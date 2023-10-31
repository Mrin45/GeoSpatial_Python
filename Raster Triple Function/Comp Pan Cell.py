#Composite
import arcpy
arcpy.env.workspace= "F:\M.tech\Python\Raster Triple Function\Comp Pan Cell"
# Perform band composition
input_layers1 = ["Blue.TIF", "Green.TIF", "Red.TIF", "NIR.TIF"]
output_Layer2 = "Composite.tif"
arcpy.CompositeBands_management(input_layers1, output_Layer2)
# Print a message indicating that the composition was successful
print("Band composition completed successfully!")
#Pan Sharpning
input_layer2 = output_Layer2
input_layer3 = "B8.TIF"
outputLayer3 = "Pan_Sharpning.tif"
arcpy.CreatePansharpenedRasterDataset_management(input_layer2,"3", "2", "1", "4", outputLayer3, input_layer3,"Esri")
mc = arcpy.GetMessageCount()
print arcpy.GetMessage(mc-1)
print("Pan Sharpning completed successfully!")

# specify the input raster dataset
in_raster = output_Layer2
# get the current cell size
current_cell_size = arcpy.env.cellSize
# set a new cell size (in meters)
new_cell_size = "10 10"
# change the cell size of the input raster dataset
arcpy.env.cellSize = new_cell_size
arcpy.management.Resample(in_raster, "resampled_raster.tif", "10 10", "NEAREST")
# reset the cell size to the original value
arcpy.env.cellSize = current_cell_size
print(" Cell Size Conversion Completed")
