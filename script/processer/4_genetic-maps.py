#!/usr/bin/python3.6
# encoding: utf-8

import sys
sys.path.append("../config")
sys.path.append("./config")
from config import *
from basics import *
from logger import Logger
from path import data_dir
from pymongo.errors import DocumentTooLarge,OperationFailure


# Script supposed to be run in the background to populate the DB with available datasets 
if "log" not in globals():
	log = Logger.init_logger('SAMPLE_DATA_%s'%(LANGUAGE_CODE), load_config())


# Script supposed to be run in the background to populate the DB with available datasets 
logger.info("Running %s",sys.argv[0])


# Get available variations and process them 
genetic_maps_to_process=genetic_maps_col.find({"mapping_file":{"$exists":False}})

logger.info("Found %d genetic map tables to process",genetic_maps_to_process.count())

for map_doc in genetic_maps_to_process:
	# on recup le chemin du fichier
	src_file= data_dir+map_doc['data_file']
	logger.info("src file: %s",src_file)
    # on recup la config du parser xls 
	parser_config=map_doc['xls_parsing']
        fileName, fileExtension = os.path.splitext(src_file)

        if fileExtension!='.xls' and fileExtension!='.xlsx':
		sheet_values = parse_tsv_table(src_file,parser_config['column_keys'],parser_config['n_rows_to_skip'],parser_config['sheet_index'])

	else:
		sheet_values = parse_excel_table(src_file,parser_config['column_keys'],parser_config['n_rows_to_skip'],parser_config['sheet_index'])

	
	try:
    	genetic_maps_col.update({"_id":map_doc['_id']},{"$set":{"mapping_file":sheet_values}})
		#break
	except DocumentTooLarge:
		print "Oops! Document too large to insert as bson object. Use grid fs to store file..."
		file=open(src_file, 'rb')
		with fs.new_file(data_file=src_file,content_type='text/plain',  metadata=dict(src=map_doc['src'],tgt=map_doc['tgt'],n_rows_to_skip=parser_config['n_rows_to_skip'])) as fp:
			fp.write(file)
		## adding fs file to the collection
		logger.info("Successfully add new file in grid fs mongo system %s",len(sheet_values))

		genetic_maps_col.update({"_id":map_doc['_id']},{"$set":{"mapping_file":{"species":species,"file":fp.data_file}}})
		# Close opened file
		file.close()


logger.info("Indexation on field \"mapping_file.Map ID\" from collection \"genetic maps\"")
variations_col.create_index("mapping_file.Map ID",sparse=True)