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
qtls_col.drop()



###################################################################################################################
############################################ PRUNUS ###############################################################
###################################################################################################################
qtl_table={
	"data_file":"Prunus/QTL/prunus_species_qtl.tsv",
	"src":"QTL ID",
	"src_version":"",
        "tgt":"Marker ID",
	"url":"http://www.rosaceae.org/node/1534497/",
	"doi":"none",
	"key":"",
	# parser config 
		# xls parser configuration, are propagated to all entries in  "experimental_results",
	"xls_parsing":{
		"n_rows_to_skip":1,
		"column_keys":['idx','HREF_QTL','QTL ID','Published Symbol','Trait Name','Trait Alias','Study','Population','HREF_col_markers','Colocalizing marker','HREF_markers','Marker ID','Map ID','AD ratio','R2','Species','Citation'],
		"sheet_index":0,
	}
}
qtls_col.insert(qtl_table)


###################################################################################################################
############################################ CUCUMIS MELO #########################################################
###################################################################################################################
qtl_table={
	"data_file":"Cucumis/QTL/QTL_physical_positions.tsv",
	"src":"QTL ID",
	"src_version":"Melonomics",
        "tgt":"Marker ID",
	"url":"",
	"doi":"none",
        "species":"Cucumis melo",
	"key":"",
	# parser config 
		# xls parser configuration, are propagated to all entries in  "experimental_results",
	"xls_parsing":{
		"n_rows_to_skip":0,
		"column_keys":['idx','Alias','QTL Name','letter_exp','QTL ID','Chromosome','Map ID','Marker ID','Marker ID 2','Start','End'],
		"sheet_index":0,
	}
}
qtls_col.insert(qtl_table)



###################################################################################################################
############################################ Hordeum Vulgare #########################################################
###################################################################################################################
qtl_table={
	"data_file":"Hordeum/QTL/QTL_physical_positions.tsv",
	"src":"QTL ID",
	"src_version":"Melonomics",
        "tgt":"Marker ID",
	"url":"",
	"doi":"none",
        "species":"Cucumis melo",
	"key":"",
	# parser config 
		# xls parser configuration, are propagated to all entries in  "experimental_results",
	"xls_parsing":{
		"n_rows_to_skip":0,
		"column_keys":['idx','Alias','QTL Name','QTL ID','Chromosome','Map ID','Marker ID','Marker ID 2','Start','End'],
		"sheet_index":0,
	}
}
qtls_col.insert(qtl_table)