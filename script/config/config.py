import pymongo
from pymongo import MongoClient

LANGUAGE_CODE = 'en-us'

client = MongoClient()
db = client.cobra_db
species_col = db.species
mappings_col = db.mappings
full_mappings_col=db.full_mappings
publications_col= db.publications
samples_col=db.samples
measurements_col=db.measurements
pv_interactions_col=db.pv_interactions
pp_interactions_col=db.pp_interactions
viruses_col=db.viruses
orthologs_col=db.orthologs
gene_ontology_col=db.gene_ontology
go_enrichments_col=db.go_enrichments
users_col=db.users
sequences_col=db.sequences
variations_col=db.variations
genetic_maps_col=db.genetic_maps
genetic_markers_col=db.genetic_markers
qtls_col=db.qtls
kegg_pathway_col=db.kegg_pathways