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

# Include all original tags with the lukr: prefix
	for k, v in attrs.iteritems():
		tags.update({'lukr:'+k:v})
#	tags.update({'lukr:raw':str(attrs)}) #all lukr original tags, including the unique ObjectId.
	
	#tags on all paths
	tags.update({'source':'lukr', 'source:date':'2010-09-17'})
	tags.update({'lukr:highway':'footway'}) #remove the lukr: prefix when the path has been reviewed.
	tags.update({'bicycle':'yes'}) #bicycles are allowed on all roads
	
	#add width if it's not zero
	if attrs['BREIDD'] != '  0.00':
		tags.update({'width':attrs['BREIDD'].lstrip()})
	
#Stigaflokkur see http://www.gamli.umhverfissvid.is/Files/Skra_0014564.pdf
#This classification system for pathways is for administrative use.
	if attrs['STIGAFLOKK'] == '4':#Malarstigur / gravel path
		tags.update({'surface':'gravel'})
#	elif attrs['STIGAFLOKK'] == '1':#Adalstigur / main path
#		tags.update({'lukr:highway':'path'}) # already added	
#	elif attrs['STIGAFLOKK'] == '2':#Tengistigur / secondary path, http://www.althingi.is/altext/125/s/0760.html
#		tags.update({'lukr:highway':'tengistigur'})
#	elif attrs['STIGAFLOKK'] == '3':#Adrir stigar
#		tags.update({'lukr:highway':'unclassified'})
	
#Tegund
	if attrs['TEG'] == '2':#Stett
		tags.update({'surface':'paved'})
	elif attrs['TEG'] == '3':#Hitaveitustigur
		tags.update({'man_made':'pipeline','location':'overground','type':'hot_water'})
	elif attrs['TEG'] == '4':#Malarstigur
		tags.update({'surface':'gravel'})
#	elif attrs['TEG'] == '1':#Stigur
#		tags.update({'lukr:highway':'path'}) # already added
	
#Flokkur
	if attrs['FLOKKUR'] == '217':#midlinur stettar
		tags.update({'surface':'paved'})
#	elif attrs['FLOKKUR'] == '215':#midlinur stigs
#		tags.update({'highway':'path'})
	
	return tags

