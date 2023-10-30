import arcpy
from arcpy.sa import *
arcpy.env.workspace = "F:\M.tech\Python\Raster Double Function\Ndvi and Clip"

red_band_raster = ("Red.TIF")
nir_band_raster = ("NIR.TIF")

#Calculating NDVI float raster
ndvi_raster = Divide(Float(Raster(nir_band_raster) - Raster(red_band_raster)), Float(Raster(nir_band_raster) + Raster(red_band_raster)))

#Saving raster:
ndvi_raster.save("NVDI.tif")
print("NDVI Completed")

# CLIP
clip_features = "F:\M.tech\Python\Guwahati_Ward\Guwahati_Ward.shp"
output_raster = "NDVI_Clipped.tif"
# Execute the Clip tool
arcpy.Clip_management("NVDI.tif","#", output_raster,clip_features,"#", "clippingGeometry")
print("Task Completed")
