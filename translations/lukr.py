"""
Translation rules for bycycle parking data from LUKR, the Reykjavik GIS department.

Usage:

./ogr2osm.py -t lukr ../Hjolraeidastaedi_HBsv_shapefile_20140701/hjolreidastaedi.shp

"""

def translateAttributes(attrs):
	if not attrs: return
	
	tags = {}

# Include all original tags with the lukr: prefix
	for k, v in attrs.iteritems():
		tags.update({'ref:hjolastaedi:'+k:v})
	
	# tags for all bike parking nodes
	tags.update({'source':'lukr', 'source:date':'2014-06-30'})
	tags.update({'amenity':'bicycle_parking'})
	
	# type of bicycle parking
	if attrs['Tegund'] == 'bogar':
		tags.update({'bicycle_parking':'wall_loops'})
	else: #TODO: the rest
		tags.update({'bicycle_parking':'stands'})
	
	return tags

