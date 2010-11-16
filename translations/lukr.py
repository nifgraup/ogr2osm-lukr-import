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
	
	#fyrir allt
	tags = {'lukr:highway':'path','foot':'designated','bicycle':'yes'}
	
	if attrs['OBJECTID']:
		tags.update({'lukr:objectid':attrs['OBJECTID']})
	
	if attrs['BREIDD'] != '  0.00':
		tags = {'width':attrs['BREIDD'].lstrip()}
	
	#do we need data precision
	#if attrs['NAKV']:
	#	tags.update({'precision':attrs['NAKV'].lstrip()})
		
	#Stigaflokkur see http://www.gamli.umhverfissvid.is/Files/Skra_0014564.pdf
	if attrs['STIGAFLOKK'] == '1':#Adalstigur / main path
		tags.update({'lukr:highway':'path'}) # already added
		
	elif attrs['STIGAFLOKK'] == '2':#Tengistigur / secondary path, http://www.althingi.is/altext/125/s/0760.html
		tags.update({'lukr:highway':'tengistigur'})
	
	elif attrs['STIGAFLOKK'] == '3':#Adrir stigar
		tags.update({'lukr:highway':'unclassified'})
	
	elif attrs['STIGAFLOKK'] == '4':#Malarstigur / gravel path
		tags.update({'surface':'gravel'})
	#or	tags.update({'surface':'unpaved'})

	
	#Tegund
	if attrs['TEG'] == '1':#Stigur
		tags.update({'lukr:highway':'path'}) # already added
		
	elif attrs['TEG'] == '2':#Stett
		tags.update({'lukr:highway':'footway'})
	
	elif attrs['TEG'] == '3':#Hitaveitustigur
		tags.update({'man_made':'pipeline','location':'overground','type':'hot_water'})
	
	elif attrs['TEG'] == '4':#Malarstigur
		tags.update({'surface':'gravel'})
	#or	tags.update({'surface':'unpaved'})
	
	return tags

