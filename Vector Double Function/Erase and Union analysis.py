import arcpy

# set the workspace
arcpy.env.workspace = "F:\M.tech\Python\Erase & Union"

# set the input & output feature class(erase)
input_fc = "IND_adm0.shp"
input_erase = "Assam.shp"
output_erase = "Erase_Out.shp"

# perform an erase analysis
arcpy.Erase_analysis(input_fc, input_erase, output_erase)

# set the output feature class(Union)
output_union = "Union_Output.shp"

# perform a union analysis
arcpy.Union_analysis([output_erase, input_erase], output_union)