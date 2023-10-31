import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "F:\M.tech\Python\Raster Triple Function\PCA NDVI NDMI"
arcpy.env.overwriteOutput = True
input_raster = ["Red.TIF","Blue.TIF","Green.TIF"]

output_raster = PrincipalComponents(input_raster)
output_raster.save("pcaoutput.tif")
print("PCA Completed")

#NDVI = Band 5 - Band 4 / Band 5 + Band 4
Band_4 = ("Red.TIF")
Band_5 = ("NIR.TIF")
#Calculating NDVI float raster

ndvi_raster = Divide(Float(Raster(Band_5) - Raster(Band_4)), Float(Raster(Band_5) + Raster(Band_4)))
#Saving raster:
ndvi_raster.save("NDVI.tif")
print("NDVI Completed")

#NDMI = Band 6 - Band 7 / Band 6 + Band 7
Band_6 = ("B6.TIF")
Band_7 = ("B7.TIF")
#Calculating NDVI float raster
ndmi_raster = Divide(
    Float(Raster(Band_6) - Raster(Band_7)), Float(Raster(Band_6) + Raster(Band_7)))
#Saving raster:
ndmi_raster.save("NDMI.tif")
print("NDMI Completed")
