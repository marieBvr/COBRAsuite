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

# Clear db
gene_ontology_col.drop()

##Mapping Prunus Domestica
mapping_table={
	"data_file":"gene_ontology/obo/gene_ontology.obo",
	"type":"rdf/XML",
	"url":"",
	"doi":"",
}
gene_ontology_col.insert(mapping_table)