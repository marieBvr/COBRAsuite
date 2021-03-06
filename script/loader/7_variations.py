#!/usr/bin/python3.6
# encoding: utf-8

import sys
sys.path.append("../config")
sys.path.append("./config")
from config import *
from basics import load_config
from logger import Logger
from random import *

# Script
if "log" not in globals():
  log = Logger.init_logger('SAMPLE_DATA_%s'%(LANGUAGE_CODE), load_config())

# Clear collections to fill
variations_col.drop()

###################################################################################################################
############################################ PRUNUS ###############################################################
###################################################################################################################

variation_table={
	"data_file":"Prunus/prunus_persica/SNP/IRSC_9K_peach_SNP_array_work_version.xls",
	"species":"Prunus persica",
	"src":"Gene ID",
	"src_version":"International Rosaceae SNP Consortium (IRSC)",
        "tgt":"Variant ID",
        "description":"""This file contains the SNPs selected for inclusion on the International 
        	Rosaceae SNP Consortium (IRSC) Peach  SNP Infinium Array that is currently in production. 
        	For more information on array design  contact Dorrie Main (dorrie@wsu.edu)""",
        "chrom":"all",
	"url":"",
	"doi":"none",
	"key":"",
	# parser config 
		# xls parser configuration, are propagated to all entries in  "experimental_results",
	"xls_parsing":{
		"n_rows_to_skip":3,
		"column_keys":['idx','Variant ID','Alleles','Scaffold','Position',],
		"sheet_index":0,
	}
}
variations_col.insert(variation_table)