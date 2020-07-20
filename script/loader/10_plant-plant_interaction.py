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
pp_interactions_col.remove({"src":"Gene ID","species":"Solanum lycopersicum"})
pp_interactions_col.remove({"src":"Uniprot ID"})
pp_interactions_col.remove({"src":"Gene ID","species":"Arabidopsis thaliana"})



##################################################################
################## BIOGRID Plant-plant interactions ##############
##################################################################

interactions_table={
	"data_file":"interactomics/biogrid/BIOGRID-ORGANISM-Solanum_lycopersicum-3.5.173.tab.xls",
	"src":"Gene ID",
	"tgt":"Gene ID 2",
	"src_symbol":"OFFICIAL_SYMBOL_A",
	"tgt_symbol":"OFFICIAL_SYMBOL_B",
    "origin":"BIOGRID",
	"type":"symbol_to_symbol",
	"species":"Solanum lycopersicum",
	"xls_parsing":{
		"n_rows_to_skip":0,
		"column_keys":['idx','Gene ID','Gene ID 2','OFFICIAL_SYMBOL_A','OFFICIAL_SYMBOL_B','ALIASES_FOR_A','ALIASES_FOR_B','EXPERIMENTAL_SYSTEM','SOURCE','PUBMED_ID','ORGANISM_A_ID','ORGANISM_B_ID'],
		"sheet_index":0,
	}

}
pp_interactions_col.insert(interactions_table)


interactions_table={
	"data_file":"interactomics/biogrid/BIOGRID-ORGANISM-Arabidopsis_thaliana_Columbia-3.5.173.tab.xls",
	"src":"Gene ID",
	"tgt":"Gene ID 2",
	"src_symbol":"OFFICIAL_SYMBOL_A",
	"tgt_symbol":"OFFICIAL_SYMBOL_B",
    "origin":"BIOGRID",
	"type":"symbol_to_symbol",
	"species":"Arabidopsis thaliana",
	"xls_parsing":{
		"n_rows_to_skip":0,
		"column_keys":['idx','Gene ID','Gene ID 2','OFFICIAL_SYMBOL_A','OFFICIAL_SYMBOL_B','ALIASES_FOR_A','ALIASES_FOR_B','EXPERIMENTAL_SYSTEM','SOURCE','PUBMED_ID','ORGANISM_A_ID','ORGANISM_B_ID'],
		"sheet_index":0,
		
	}

}
pp_interactions_col.insert(interactions_table)


##################################################################
################## INTACT ########################################
##################################################################
interactions_table={
	"data_file":"interactomics/Intact/intact_full.xls",
	"type":"intact",
	"src":"Uniprot ID",
	"src_version":"uniprot",
	"tgt":"Uniprot ID 2",
	"tgt_version":"uniprot",
	"src_name":"Taxid interactor A",
	"tgt_name":"Taxid interactor B",
    "origin":"INTACT",
	"method":"detection_method",
	"pub":"pmid",
	"xls_parsing":{
		"n_rows_to_skip":0,
		"column_keys":['idx','protein_EBI_ref_1','protein_EBI_ref_2','Uniprot ID','Uniprot ID 2','alternative_identifiers_1','alternative_identifiers_2','detection_method','author_name','pmid','Taxid interactor A','Taxid interactor B','interaction_type','source_database_id','interaction_identifier','confidence'],
		"sheet_index":0,
		
	}

}
pp_interactions_col.insert(interactions_table)


