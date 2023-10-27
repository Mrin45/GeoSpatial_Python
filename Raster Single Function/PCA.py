import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "F:\M.tech\Python\Raster Single Function\PCA"
arcpy.env.overwriteOutput = True
input_raster = ["Red.TIF","Blue.TIF","Green.TIF"]

output_raster = PrincipalComponents(input_raster)
output_raster.save("pcaoutput.tif")
print("PCA Completed")
