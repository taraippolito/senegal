# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# define_projection_senegal.py
# Created on: 2021-06-01 12:28:14.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

files = ['C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_bdod_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_bdod_0-5_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_bdod_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_bdod_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_bdod_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_bdod_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_bdod_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cec_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cec_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cec_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cec_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cec_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cec_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cfvo_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cfvo_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cfvo_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cfvo_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cfvo_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_cfvo_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_clay_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_clay_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_clay_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_clay_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_clay_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_clay_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_nitrogen_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_nitrogen_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_nitrogen_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_nitrogen_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_nitrogen_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_nitrogen_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_phh2o_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_phh2o_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_phh2o_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_phh2o_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_phh2o_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_phh2o_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_sand_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_sand_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_sand_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_sand_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_sand_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_sand_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_silt_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_silt_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_silt_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_silt_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_silt_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_silt_60-100cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_soc_0-5cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_soc_100-200cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_soc_15-30cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_soc_30-60cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_soc_5-15cm_mean.tif', 'C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\SG_data\\Senegal_soc_60-100cm_mean.tif']


# # Local variables:
# # file that you would choose in arcmap
# Senegal_bdod_0_5_mean_tif = "Senegal_bdod_0-5_mean.tif"
# Senegal_bdod_0_5_mean_tif__2_ = Senegal_bdod_0_5_mean_tif

# # Process: Define Projection
# arcpy.DefineProjection_management(Senegal_bdod_0_5_mean_tif, "PROJCS['World_Goode_Homolosine_Land',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Goode_Homolosine'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Option',1.0],UNIT['Meter',1.0]]")

for file in files: 
    run_file = file
    arcpy.DefineProjection_management(run_file, "PROJCS['World_Goode_Homolosine_Land',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Goode_Homolosine'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Option',1.0],UNIT['Meter',1.0]]")

