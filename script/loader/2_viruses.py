#!/usr/bin/python3.6
# encoding: utf-8

import sys
sys.path.append("../config")
sys.path.append("./config")
from config import *
from basics import load_config
from logger import Logger
from random import *

# Script
if "log" not in globals():
  log = Logger.init_logger('SAMPLE_DATA_%s'%(LANGUAGE_CODE), load_config())

# clear db 
viruses_col.remove()

####Viruses

### Virus to add 
#PepMV, ToCV, TSWV, PVY for tomato
#LMV, TuMV and arabidopsis
#BaYMV BaMMV, BYDV, CYDV in barley


m_canon={
	"full_name":"Monosporascus Cannonballus",
	"abbrev_name":"M. canonballus",
	"aliases":["monosporascus_cannonballus"],
	"taxid":155416,
	"classification":{
		"top_level":"Eukaryotes",
		"kingdom":	"Fungi",
		"phylum":	"Ascomycota",
		"class":	"Sordariomycetes",
		"subclass":	"Sordariomycetidae",
		"order":	"Sordariales",
		"family":	"Incertae sedis",
		"genus":	"Monosporascus",
		"species": "M. cannonballus"
	},
	"wikipedia":"http://en.wikipedia.org/wiki/Monosporascus_cannonballus"
}
viruses_col.insert(m_canon)

rgsv={
	"full_name":"Rice grassy stunt virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Rice_grassy_stunt_virus",
	"aliases":['rgsv','rice rosette Philippines virus'],
	"classification":{
		"top_level":"viruses",
		"group":"Group V ((-)ssRNA)",
		"genus":"Tenuivirus",
		"species":"Rice grassy stunt virus",
	}
	
}
viruses_col.insert(rgsv)


rdv={
	"full_name":"Rice dwarf virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Rice_dwarf_virus",
	"aliases":['rdv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group III (dsRNA)",
		"order":"Unassigned",
		"family":"Reoviridae",
		"genus":"Phytoreovirus",
		"species":"Rice dwarf virus",
	}
	
}

viruses_col.insert(rdv)

scmv={
	"full_name":"Sugarcane mosaic virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Sugarcane_mosaic_virus",
	"aliases":['scmv','grass mosaic virus'
,'maize dwarf mosaic virus strain B',
'sorghum red stripe virus'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Potyviridae",
		"genus":"Potyvirus",
		"species":"Sugarcane mosaic virus",
	}
	
}

viruses_col.insert(scmv)

cmv={
	"full_name":"Cucumber mosaic virus",
	"wikipedia":"http://en.wikipedia.org/wiki/Cucumber_mosaic_virus",
	"aliases":['cmv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Bromoviridae",
		"genus":"Cucumovirus",
		"species":"Cucumber mosaic virus",
	}
	
}
viruses_col.insert(cmv)

wmv={
	"full_name":"Watermelon mosaic virus",
	"wikipedia":"http://en.wikipedia.org/wiki/Watermelon_mosaic_virus",
	"aliases":['wmv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Potyviridae",
		"genus":"Potyvirus",
		"species":"Watermelon mosaic virus",
	}
}	
viruses_col.insert(wmv)


ppv={
	"full_name":"Plum pox virus",
	"wikipedia":"http://en.wikipedia.org/wiki/Plum_pox",
	"aliases":['sharka','ppv','Plum pox'],
	"classification":{
		"top_level":"viruses",
		"group": "Group IV ((+)ssRNA)",
		"family": "Potyviridae",
		"genus": "Potyvirus",
		"species": "Plum pox virus"
	}
	
}
viruses_col.insert(ppv)



tev={
	"full_name":"Tobacco etch virus",
	"wikipedia":"http://en.wikipedia.org/wiki/Tobacco_etch_virus",
	"aliases":['tev'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Potyviridae",
		"genus":"Potyvirus",
		"species":"Tobacco etch virus",
	}
	
}

viruses_col.insert(tev)
pvx={
	"full_name":"Potato virus X",
	"wikipedia":"https://en.wikipedia.org/wiki/Potato_virus_X",
	"aliases":['pvx','PVX'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Tymovirales",
		"family":"Alphaflexiviridae",
		"genus":"Potexvirus",
		"species":"Potato virus X",
	}
	
}
viruses_col.insert(pvx)




tmv={
	"full_name":"Tobacco mosaic virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Tobacco_mosaic_virus",
	"aliases":['tmv','TMV'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Virgaviridae",
		"genus":"Tobamovirus",
		"species":"Tobacco mosaic virus",
	}
	
}
viruses_col.insert(tmv)
bydv={
	"full_name":"Barley yellow dwarf virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Barley_yellow_dwarf",
	"aliases":['bydv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Luteoviridae",
		"genus":"Luteovirus",
		"species":"Barley yellow dwarf virus",
	}
	
}
viruses_col.insert(bydv)

bymv={
	"full_name":"Barley yellow mosaic virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Barley_yellow_mosaic_virus",
	"aliases":['bymv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Potyviridae",
		"genus":"Bymovirus",
		"species":"Barley yellow mosaic virus",
	}
	
}
viruses_col.insert(bymv)

sbcmv={
	"full_name":"Soil-borne cereal mosaic virus",
	"wikipedia":"",
	"aliases":['sbcmv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Virgaviridae",
		"genus":"Furovirus",
		"species":"Soil-borne cereal mosaic virus",
	}
	
}
viruses_col.insert(sbcmv)

sbwmv={
	"full_name":"Soil-borne wheat mosaic virus",
	"wikipedia":"",
	"aliases":['sbwmv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Virgaviridae",
		"genus":"Furovirus",
		"species":"Soil-borne wheat mosaic virus",
	}
	
}
viruses_col.insert(sbwmv)

tylcv={
	"full_name":"Tomato yellow leaf curl virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Tomato_yellow_leaf_curl_virus",
	"aliases":['tylcv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group II",
		"order":"Unassigned",
		"family":"Geminiviridae",
		"genus":"Begomovirus",
		"species":"Tomato yellow leaf curl virus",
	}
	
}
viruses_col.insert(tylcv)

lmv={
	"full_name":"Lettuce mosaic virus",
	"wikipedia":"https://en.wikipedia.org/wiki/Lettuce_mosaic_virus",
	"aliases":['lmv'],
	"classification":{
		"top_level":"viruses",
		"group": "Group IV ((+)ssRNA)",
		"family": "Potyviridae",
		"genus": "Potyvirus",
		"species": "Lettuce mosaic virus"
	}
	
}
viruses_col.insert(lmv)