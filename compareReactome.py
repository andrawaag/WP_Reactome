__author__ = 'andra'

import requests
import pprint
import pandas as pd
import sys

native_reactome_url = "http://www.reactome.org/download/current/ReactomePathways.txt"
reactome_cols = ['reactome-id', 'name', 'species']
native_reactome = pd.read_csv(native_reactome_url, sep='\t', header = None, names=reactome_cols)
human_reactome_pathways =  native_reactome[native_reactome['species'] == "Homo sapiens"] # Filter only human pathways in Reactome


wp_cols = ['name', 'wp-id']

# The reactome_in_wp.tsv file was mnanully created by downloading the zip containing all Reactome Pathways in WikiPathways
# From http://www.wikipathways.org//wpi/batchDownload.php?species=Homo%20sapiens&fileType=gpml&tag=Curation:Reactome_Approved
# and preprocessing the filenames of those GPML file into reactome_in_wp.tsv
# The following sequence of bash commands were used:
# > unzip wikipathways_Homo_sapiens_Curation-Reactome_Approved__gpml.zip
# > rm wikipathways_Homo_sapiens_Curation-Reactome_Approved__gpml.zip
# > ls >reactome_in_wp.tsv
# > cat reactome_in_wp.tsv | sed "s/\_WP/   WP/g" > reactome_in_wp.tsv
# > cat reactome_in_wp.tsv | sed "s/Hs_/Hs   /" | sed "s/.gpml//g"| sed "s/_/ /g" >reactome_in_wp.tsv
# TODO Try to get this list like with reactome without preprocessing.

wp_reactome = pd.read_csv('reactome_in_wp.tsv', sep='\t', header = None, names=wp_cols)
pprint.pprint(wp_reactome.head())

comparison = pd.merge(human_reactome_pathways, wp_reactome, on="name",  how='outer')
mapping = comparison[['reactome-id', 'wp-id']]

comparison.to_csv('Reactome_in_Wikipathways.tsv', sep='\t', encoding='utf-8')
mapping.to_csv('Reactome_in_Wikipathways_mappings_only.tsv', sep='\t', encoding='utf-8')