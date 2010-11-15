"""
Translation rules for data from LUKR, the Reykjavik GIS department.

Usage:

./ogr2osm.py -t lukr ../lukr-osm-donation-2010-09-18/gonguleidir_LUKR_170910.shp

Original attributes:

['OBJECTID', 'STIGAFLOKK', 'BREIDD', 'TEIKNINR', 'ASTAND', 'AR_LAGT', 'AR_LAGF', 'TEG', 'FLOKKUR', 'RUTT', 'AR_ADG', 'UTBSV', 'RUTT_BREID', 'DAGS_INN', 'NOTANDI', 'DAGS_BREYT', 'BREYTANDI', 'SVF', 'UPPR', 'NAKV', 'DAGS_UPPR', 'DAGS_LEIDR', 'DAGS_UPPF', 'GAGNA_EIGN', 'HEIMILD', 'NAFN_G', 'NAKV_XY', 'VIDMIDUN_P', 'VINNSLA_F', 'SHAPE_LEN']

Extra attributes can be added later if needed, as OBJECTID is unique.
"""

def translateAttributes(attrs):
	if not attrs: return
	
	tags = {}
	
	if attrs['BREIDD'] != '  0.00':
		tags = {'width':attrs['BREIDD'].lstrip()}
	
	if attrs['NAKV']:
		tags.update({'PRECISION':attrs['NAKV'].lstrip()})
	
	if attrs['OBJECTID']:
		tags.update({'lukr:objectid':attrs['OBJECTID']})
	
	#Todo: Stigaflokkur
	if attrs['STIGAFLOKK'] == '1':#Adalstigur
		tags.update({'lukr:highway':'road'})
		
	elif attrs['STIGAFLOKK'] == '2':#Tengistigur
		tags.update({'lukr:highway':'trunk'})
	
	elif attrs['STIGAFLOKK'] == '3':#Adrir stigar
		tags.update({'lukr:highway':'construction','construction':'road'})
	
	elif attrs['STIGAFLOKK'] == '4':#Malarstigur
		tags.update({'surface':'unpaved'})
	
	#Todo: Tegund
	if attrs['TEG'] == '1':#Stigur
		tags.update({'lukr:highway':'path'})
		
	elif attrs['TEG'] == '2':#Stett
		tags.update({'lukr:highway':'trunk'})
	
	elif attrs['TEG'] == '3':#Hitaveitustigur
		tags.update({'lukr:highway':'construction','construction':'road'})
	
	elif attrs['TEG'] == '4':#Malarstigur
		tags.update({'surface':'unpaved'})
	
	return tags

