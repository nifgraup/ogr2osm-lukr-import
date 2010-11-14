"""
Translation rules for data from LUKR, the Reykjavik GIS department.
"""



def translateAttributes(attrs):
	if not attrs: return
	
	tags = {}
	
	if attrs['BREIDD']:
		tags = {'width':attrs['BREIDD']}
	
	if attrs['NAKV']:
		tags = {'PRECISION':attrs['NAKV']}
	
	if attrs['OBJECTID']:
		tags = {'lukr:objectid':attrs['OBJECTID']}
	
	#Todo: Stigaflokkur
	if attrs['STIGAFLOKK'] == '1':#Adalstigur
		tags.update({'lukr:highway':'road'})
		
	elif attrs['STIGAFLOKK'] == '2':#Tengistigur
		tags.update({'lukr:highway':'trunk'})
	
	elif attrs['STIGAFLOKK'] == '3':#Adrir stigar
		tags.update({'lukr:highway':'construction','construction':'road'})
	
	elif attrs['STIGAFLOKK'] == '4':#Malarstigur
		tags.update({'lukr:highway':'service'})
	
	#Todo: Tegund
	if attrs['TEG'] == '1':#Stigur
		tags.update({'lukr:highway':'road'})
		
	elif attrs['TEG'] == '2':#Stett
		tags.update({'lukr:highway':'trunk'})
	
	elif attrs['TEG'] == '3':#Hitaveitustigur
		tags.update({'lukr:highway':'construction','construction':'road'})
	
	elif attrs['TEG'] == '4':#Malarstigur
		tags.update({'lukr:highway':'service'})
	
	return tags

