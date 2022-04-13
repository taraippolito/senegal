# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# combine_rasters_DEM_senegal.py
# Created on: 2021-06-10 10:25:52.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
AP_07409_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0230_RT2.dem.tif"
DEM_Combined_new_tif = AP_07409_FBD_F0230_RT2_dem_tif
AP_07409_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0240_RT2.dem.tif"
AP_07409_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0250_RT2.dem.tif"
AP_07409_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0260_RT2.dem.tif"
AP_07409_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0270_RT2.dem.tif"
AP_07409_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0280_RT2.dem.tif"
AP_07409_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0290_RT2.dem.tif"
AP_07409_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0300_RT2.dem.tif"
AP_07409_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0310_RT2.dem.tif"
AP_07409_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0320_RT2.dem.tif"
AP_07511_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0230_RT2.dem.tif"
AP_07511_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0240_RT2.dem.tif"
AP_07511_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0250_RT2.dem.tif"
AP_07511_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0260_RT2.dem.tif"
AP_07511_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0270_RT2.dem.tif"
AP_07511_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0280_RT2.dem.tif"
AP_07511_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0290_RT2.dem.tif"
AP_07511_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0300_RT2.dem.tif"
AP_07584_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0230_RT2.dem.tif"
AP_07584_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0240_RT2.dem.tif"
AP_07584_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0250_RT2.dem.tif"
AP_07584_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0260_RT2.dem.tif"
AP_07584_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0270_RT2.dem.tif"
AP_07584_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0280_RT2.dem.tif"
AP_07584_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0290_RT2.dem.tif"
AP_07584_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0300_RT2.dem.tif"
AP_07584_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0310_RT2.dem.tif"
AP_07584_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0320_RT2.dem.tif"
AP_07657_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0230_RT2.dem.tif"
AP_07657_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0240_RT2.dem.tif"
AP_07657_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0250_RT2.dem.tif"
AP_07657_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0260_RT2.dem.tif"
AP_07657_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0270_RT2.dem.tif"
AP_07657_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0280_RT2.dem.tif"
AP_07657_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0290_RT2.dem.tif"
AP_07657_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0300_RT2.dem.tif"
AP_07657_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0310_RT2.dem.tif"
AP_07657_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0320_RT2.dem.tif"
AP_07730_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0230_RT2.dem.tif"
AP_07730_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0240_RT2.dem.tif"
AP_07730_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0250_RT2.dem.tif"
AP_07730_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0260_RT2.dem.tif"
AP_07730_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0270_RT2.dem.tif"
AP_07730_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0280_RT2.dem.tif"
AP_07730_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0290_RT2.dem.tif"
AP_07832_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0230_RT2.dem.tif"
AP_07832_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0240_RT2.dem.tif"
AP_07832_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0250_RT2.dem.tif"
AP_07832_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0260_RT2.dem.tif"
AP_07832_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0270_RT2.dem.tif"
AP_07832_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0280_RT2.dem.tif"
AP_07832_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0290_RT2.dem.tif"
AP_07832_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0300_RT2.dem.tif"
AP_07832_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0310_RT2.dem.tif"
AP_07832_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0320_RT2.dem.tif"
AP_07905_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0230_RT2.dem.tif"
AP_07905_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0240_RT2.dem.tif"
AP_07905_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0250_RT2.dem.tif"
AP_07905_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0260_RT2.dem.tif"
AP_07905_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0270_RT2.dem.tif"
AP_07905_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0280_RT2.dem.tif"
AP_07905_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0290_RT2.dem.tif"
AP_07905_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0300_RT2.dem.tif"
AP_07905_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0310_RT2.dem.tif"
AP_07978_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07978_FBD_F0280_RT2.dem.tif"
AP_08007_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0230_RT2.dem.tif"
AP_08007_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0240_RT2.dem.tif"
AP_08007_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0250_RT2.dem.tif"
AP_08007_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0260_RT2.dem.tif"
AP_08007_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0270_RT2.dem.tif"
AP_08007_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0280_RT2.dem.tif"
AP_08007_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0290_RT2.dem.tif"
AP_08007_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0300_RT2.dem.tif"
AP_08007_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0310_RT2.dem.tif"
AP_08007_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0320_RT2.dem.tif"
AP_08080_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0230_RT2.dem.tif"
AP_08080_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0240_RT2.dem.tif"
AP_08080_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0250_RT2.dem.tif"
AP_08080_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0260_RT2.dem.tif"
AP_08080_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0270_RT2.dem.tif"
AP_08080_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0280_RT2.dem.tif"
AP_08080_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0290_RT2.dem.tif"
AP_08080_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0300_RT2.dem.tif"
AP_08080_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0310_RT2.dem.tif"
AP_08080_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0320_RT2.dem.tif"
AP_08153_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0230_RT2.dem.tif"
AP_08153_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0240_RT2.dem.tif"
AP_08153_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0250_RT2.dem.tif"
AP_08153_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0260_RT2.dem.tif"
AP_08153_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0270_RT2.dem.tif"
AP_08153_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0280_RT2.dem.tif"
AP_08153_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0290_RT2.dem.tif"
AP_08153_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0300_RT2.dem.tif"
AP_08153_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0310_RT2.dem.tif"
AP_08182_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0230_RT2.dem.tif"
AP_08182_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0240_RT2.dem.tif"
AP_08182_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0250_RT2.dem.tif"
AP_08182_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0260_RT2.dem.tif"
AP_08182_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0270_RT2.dem.tif"
AP_08182_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0280_RT2.dem.tif"
AP_08182_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0290_RT2.dem.tif"
AP_08182_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0300_RT2.dem.tif"
AP_08328_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0230_RT2.dem.tif"
AP_08328_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0240_RT2.dem.tif"
AP_08328_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0250_RT2.dem.tif"
AP_08328_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0260_RT2.dem.tif"
AP_08328_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0270_RT2.dem.tif"
AP_08328_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0280_RT2.dem.tif"
AP_08328_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0290_RT2.dem.tif"
AP_08328_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0300_RT2.dem.tif"
AP_08328_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0310_RT2.dem.tif"
AP_08328_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0320_RT2.dem.tif"
AP_08401_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0230_RT2.dem.tif"
AP_08401_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0240_RT2.dem.tif"
AP_08401_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0250_RT2.dem.tif"
AP_08401_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0260_RT2.dem.tif"
AP_08401_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0270_RT2.dem.tif"
AP_08401_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0280_RT2.dem.tif"
AP_08401_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0290_RT2.dem.tif"
AP_08430_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0230_RT2.dem.tif"
AP_08430_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0240_RT2.dem.tif"
AP_08430_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0250_RT2.dem.tif"
AP_08430_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0260_RT2.dem.tif"
AP_08430_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0270_RT2.dem.tif"
AP_08430_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0280_RT2.dem.tif"
AP_08430_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0290_RT2.dem.tif"
AP_08430_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0300_RT2.dem.tif"
AP_08430_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0310_RT2.dem.tif"
AP_08503_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0230_RT2.dem.tif"
AP_08503_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0240_RT2.dem.tif"
AP_08503_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0250_RT2.dem.tif"
AP_08503_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0260_RT2.dem.tif"
AP_08503_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0270_RT2.dem.tif"
AP_08503_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0280_RT2.dem.tif"
AP_08503_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0290_RT2.dem.tif"
AP_08503_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0300_RT2.dem.tif"
AP_08503_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0310_RT2.dem.tif"
AP_08503_FBD_F0320_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0320_RT2.dem.tif"
AP_08576_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0230_RT2.dem.tif"
AP_08576_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0240_RT2.dem.tif"
AP_08576_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0250_RT2.dem.tif"
AP_08576_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0260_RT2.dem.tif"
AP_08576_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0270_RT2.dem.tif"
AP_08576_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0280_RT2.dem.tif"
AP_08576_FBD_F0290_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0290_RT2.dem.tif"
AP_08576_FBD_F0300_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0300_RT2.dem.tif"
AP_08576_FBD_F0310_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0310_RT2.dem.tif"
AP_08605_FBD_F0230_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0230_RT2.dem.tif"
AP_08605_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0240_RT2.dem.tif"
AP_08605_FBD_F0250_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0250_RT2.dem.tif"
AP_08605_FBD_F0260_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0260_RT2.dem.tif"
AP_08605_FBD_F0270_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0270_RT2.dem.tif"
AP_08605_FBD_F0280_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0280_RT2.dem.tif"
AP_09028_FBD_F0240_RT2_dem_tif = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_09028_FBD_F0240_RT2.dem.tif"
DEM = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM"

# Process: Mosaic To New Raster
arcpy.MosaicToNewRaster_management("C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07409_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07511_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07584_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07657_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07730_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07832_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07905_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_07978_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08007_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08080_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08153_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08182_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08328_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08401_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08430_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08503_FBD_F0320_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0290_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0300_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08576_FBD_F0310_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0230_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0240_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0250_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0260_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0270_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_08605_FBD_F0280_RT2.dem.tif;C:\\Users\\Research\\Documents\\Tara_Fall_2019\\Senegal_LCC\\DEM\\AP_09028_FBD_F0240_RT2.dem.tif", DEM, "DEM_Combined_new.tif", "", "16_BIT_SIGNED", "", "1", "LAST", "FIRST")

