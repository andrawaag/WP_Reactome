__author__ = 'andra'

import requests
import pprint
import pandas as pd
import sys

native_reactome_url = "http://www.reactome.org/download/current/ReactomePathways.txt"
reactome_cols = ['reactome-id', 'name', 'species']
native_reactome = pd.read_csv(native_reactome_url, sep='\t', header = None, names=reactome_cols)
human_reactome_pathways =  native_reactome[native_reactome['species'] == "Homo sapiens"]

pprint.pprint(human_reactome_pathways.head())

wp_cols = ['name', 'wp-id']
wp_reactome = pd.read_csv('reactome_in_wp.tsv', sep='\t', header = None, names=wp_cols)
pprint.pprint(wp_reactome.head())

comparison = pd.merge(human_reactome_pathways, wp_reactome, on="name",  how='outer')
mapping = comparison[['reactome-id', 'wp-id']]

comparison.to_csv('Reactome_in_Wikipathways.tsv', sep='\t', encoding='utf-8')
mapping.to_csv('Reactome_in_Wikipathways_mappings_only.tsv', sep='\t', encoding='utf-8')