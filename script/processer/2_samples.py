#!/usr/bin/python3.6
# encoding: utf-8

import sys
sys.path.append("../config")
sys.path.append("./config")
from config import *
from basics import *
from logger import Logger
import string
from random import *
from numbers import Number
import collections
from math import log
from path import data_dir
from pymongo.errors import DocumentTooLarge,OperationFailure

# Script 
import datetime
if "log" not in globals():
  log = Logger.init_logger('SAMPLE_DATA_%s'%(LANGUAGE_CODE), load_config())

logger.info("Running %s",sys.argv[0])

# Get available datasets and insert them in the DB 
samples_to_process=samples_col.find({"experimental_results":{"$elemMatch":{"values":{"$exists":False}}}})

logger.info("Found %d samples to process",samples_to_process.count())

for a_sample in samples_to_process:
        
	logger.info("Will process dataset for experiment %s",a_sample['name'])
	parser_config=a_sample['xls_parsing']
	for a_result_idx,a_result in [(i,x) for i,x in enumerate(a_sample['experimental_results']) if "values" not in x]:
		# specialize parser for the result 
		logger.info("Will process results from file %s sheet %d",a_result['data_file'],parser_config['sheet_index'])
		parser_config.update(a_result.get('xls_parsing',{}))
        src_file= data_dir+a_result['data_file']
        fileName, fileExtension = os.path.splitext(src_file)
        if fileExtension=='.xls' or fileExtension=='.xlsx' or fileExtension=='.XLS' :
            parsed_data = parse_excel_table(src_file,parser_config['column_keys'],parser_config['n_rows_to_skip'],parser_config['sheet_index'],parser_config['id_type'])

        else:
            parsed_data = parse_tsv_table(src_file,parser_config['column_keys'],parser_config['n_rows_to_skip'],parser_config['id_type'])
		# perform the mapping 
        try:
            diagnostic=samples_col.update({"_id":a_sample['_id'],"experimental_results.data_file":a_result['data_file']},{"$set":{"experimental_results.$.values":parsed_data}})
            logger.info("Performed insertion:%s",diagnostic)
        except DocumentTooLarge:
            print "Oops! Document too large to insert as bson object. Use grid fs to store file..."

