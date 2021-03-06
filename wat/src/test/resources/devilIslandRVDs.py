#!/usr/bin/python3

import getpass

import requests
import json
#from pprint import pprint

username = input("%-- >> Username : ")
password = getpass.getpass("%-- >> Password : ")
srvurl = input("%-- >> Ariane server url (like http://serverFQDN:6969/) : ")

# CREATE REQUESTS SESSION
s = requests.Session()
s.auth = (username, password)


## CREATE LAN RVD APP6969 RVD 21
containerParams = {'primaryAdminURL':'http://app6969rvd21.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.app6969rvd21'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')
rvd21 = containerID

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.47.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan3'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","71ab90"], "name":["String","DEV APP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","app6969rvd21"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)


## ADD A GATE TO LAN APP6969 RVD 21
gateParams = {"URL":"http://app6969rvd21.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.app6969rvd21", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

nodeParams = {"name":"APP6969.RVD21", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')


#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'APP FX prices diffusion'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)


## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://app6969rvd21.lab02.dev.dekatonshivr.echinopsii.net/;239.69.69.69:6969", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)


## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.69.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams);






## CREATE LAN RVD APP6969 RVD 22
containerParams = {'primaryAdminURL':'http://app6969rvd22.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.app6969rvd22'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')
rvd22 = containerID

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.47.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan3'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","71ab90"], "name":["String","DEV APP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","app6969rvd22"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)


## ADD A GATE TO LAN APP6969 RVD 22
gateParams = {"URL":"http://app6969rvd22.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.app6969rvd22", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

nodeParams = {"name":"APP6969.RVD22", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')


#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'APP FX prices diffusion'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)


## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://app6969rvd22.lab02.dev.dekatonshivr.echinopsii.net/;239.69.69.69:6969", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)


## LINK ENDPOINT TO MULTICAST TRANSPORT
linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams);






## CREATE LAN RVD APP6969 RVD 23
containerParams = {'primaryAdminURL':'http://app6969rvd23.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.app6969rvd23'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')
rvd23 = containerID

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.48.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan4'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","71ab90"], "name":["String","DEV APP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","app6969rvd23"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)


## ADD A GATE TO LAN APP6969 RVD 23
gateParams = {"URL":"http://app6969rvd23.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.app6969rvd23", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

nodeParams = {"name":"APP6969.RVD23", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')


#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'APP FX prices diffusion'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)


## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://app6969rvd23.lab02.dev.dekatonshivr.echinopsii.net/;239.69.69.69:6969", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)


## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.69.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams);






## CREATE LAN RVD APP6969 RVD 24
containerParams = {'primaryAdminURL':'http://app6969rvd24.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.app6969rvd24'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')
rvd24 = containerID

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.48.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan4'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","71ab90"], "name":["String","DEV APP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","app6969rvd24"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)


## ADD A GATE TO LAN APP6969 RVD 24
gateParams = {"URL":"http://app6969rvd24.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.app6969rvd24", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

## ADD A NODE TO LAN APP6969 RVD 24
nodeParams = {"name":"APP6969.RVD24", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')


#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'APP FX prices diffusion'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)


## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://app6969rvd24.lab02.dev.dekatonshivr.echinopsii.net/;239.69.69.69:6969", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","e3a164"], "name":["String","APP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)


## LINK ENDPOINT TO MULTICAST TRANSPORT
linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams)



## CREATE LAN RVD BPP6669 RVD 21
containerParams = {'primaryAdminURL':'http://bpp6669rvd21.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.bpp6669rvd21'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.49.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan5'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","ad853b"], "name":["String","DEV BPP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","bpp6669rvd21"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

## ADD A GATE TO LAN BPP6669 RVD 21
gateParams = {"URL":"http://bpp6669rvd21.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.bpp6669rvd21", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

## ADD A NODE TO LAN BPP6669 RVD 21
nodeParams = {"name":"BPP6669.RVD21", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')

#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'BPP FX prices historization'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://bpp6669rvd21.lab02.dev.dekatonshivr.echinopsii.net/;239.69.66.69:6669", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)

## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.66.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

transportProperty = {'ID':transportID,'propertyName':'busDescription','propertyValue':'BPP FX prices historization'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/update/properties/add', params=transportProperty)

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
transportProperty = {'ID':transportID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/update/properties/add', params=transportProperty)

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams)




## CREATE LAN RVD BPP6669 RVD 22
containerParams = {'primaryAdminURL':'http://bpp6669rvd22.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.bpp6669rvd22'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.49.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan5'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","ad853b"], "name":["String","DEV BPP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","bpp6669rvd22"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

## ADD A GATE TO LAN BPP6669 RVD 22
gateParams = {"URL":"http://bpp6669rvd22.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.bpp6669rvd22", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

## ADD A NODE TO LAN BPP6669 RVD 22
nodeParams = {"name":"BPP6669.RVD22", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')

#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'BPP FX prices historization'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://bpp6669rvd22.lab02.dev.dekatonshivr.echinopsii.net/;239.69.66.69:6669", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)

## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.66.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams)

## ADD A NODE TO LAN BPP6669 RVD 22
nodeParams = {"name":"BRDG-6969-6669.RVD22", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')

#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'BPP FX prices historization'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://bpp6669rvd22.lab02.dev.dekatonshivr.echinopsii.net/;239.69.69.69:6969", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)

## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.69.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams)


## CREATE LAN RVD BPP6669 RVD 23
containerParams = {'primaryAdminURL':'http://bpp6669rvd23.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.bpp6669rvd23'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.50.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan6'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","ad853b"], "name":["String","DEV BPP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","bpp6669rvd23"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

## ADD A GATE TO LAN BPP6669 RVD 23
gateParams = {"URL":"http://bpp6669rvd23.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.bpp6669rvd23", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

## ADD A NODE TO LAN BPP6669 RVD 23
nodeParams = {"name":"BPP6669.RVD23", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')

#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'BPP FX prices historization'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://bpp6669rvd23.lab02.dev.dekatonshivr.echinopsii.net/;239.69.66.69:6669", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)

## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.66.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams)



## CREATE LAN RVD BPP6669 RVD 24
containerParams = {'primaryAdminURL':'http://bpp6669rvd24.lab02.dev.dekatonshivr.echinopsii.net:7580', 'primaryAdminGateName':'webadmingate.bpp6669rvd24'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/create', params=containerParams)
containerID = r.json().get('containerID')

# MANDATORY FOR GRAPH RENDER
containerCompany = {'ID':containerID,'company':'Tibco'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/company', params=containerCompany)

containerProduct = {'ID':containerID,'product':'Tibco Rendez Vous'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/product', params=containerProduct)

containerType = {'ID':containerID,'type':'RV Daemon'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/type', params=containerType)

datacenter = {"dc":["String","Somewhere in hell [DR]"], "gpsLng":["double",-52.582179], "address":["String","Devil's Island"], "gpsLat":["double",5.295366], "town":["String","Devil's Island"], "country":["String","France"]}
containerProperty = {'ID':containerID,'propertyName':'Datacenter','propertyValue':json.dumps(datacenter),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

network = {'subnetip':['String','192.168.50.0'], 'subnetmask':['String','255.255.255.0'], 'type':['String','LAN'], 'lan':['String','lab02.lan6'], 'marea':['String',"devil's mind"]}
containerProperty = {'ID':containerID,'propertyName':'Network','propertyValue':json.dumps(network),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

supportTeam = {"color":["String","ad853b"], "name":["String","DEV BPP"]}
containerProperty = {'ID':containerID,'propertyName':'supportTeam','propertyValue':json.dumps(supportTeam),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

server = { "os":["String","Fedora 18 - x86_64"], "hostname":["String","bpp6669rvd24"] }
containerProperty = {'ID':containerID,'propertyName':'Server','propertyValue':json.dumps(server),'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/containers/update/properties/add', params=containerProperty)

## ADD A GATE TO LAN BPP6669 RVD 24
gateParams = {"URL":"http://bpp6669rvd24.lab02.dev.dekatonshivr.echinopsii.net:7500", "name":"rvdgate.bpp6669rvd24", "containerID":containerID, "isPrimaryAdmin":False}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/gates/create', params=gateParams)

## ADD A NODE TO LAN BPP6669 RVD 24
nodeParams = {"name":"BPP6669.RVD24", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')

#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'BPP FX prices historization'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://bpp6669rvd24.lab02.dev.dekatonshivr.echinopsii.net/;239.69.66.69:6669", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)

## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.66.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams)

## ADD A NODE TO LAN BPP6669 RVD 24
nodeParams = {"name":"BRDG-6969-6669.RVD24", "containerID":containerID, "parentNodeID":0}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/create', params=nodeParams)
nodeID = r.json().get('nodeID')

#OPTIONAL NODE PROPERTIES (BUT USEFULL)
nodeProperty = {'ID':nodeID,'propertyName':'busDescription','propertyValue':'BPP FX prices historization'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
nodeProperty = {'ID':nodeID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/nodes/update/properties/add', params=nodeProperty)

## ADD ENDPOINT TO PREVIOUS NODE
endpointParams = {"endpointURL":"multicast-udp-tibrv://bpp6669rvd24.lab02.dev.dekatonshivr.echinopsii.net/;239.69.69.69:6669", "parentNodeID":nodeID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/create', params=endpointParams)
endpointID = r.json().get('endpointID')

primaryApp = {"color":["String","852e48"], "name":["String","BPP"]}
endpointProperty = {'ID':endpointID,'propertyName':'primaryApplication','propertyValue':json.dumps(primaryApp), 'propertyType':'map'}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/endpoints/update/properties/add', params=endpointProperty)

## LINK ENDPOINT TO MULTICAST TRANSPORT
transportParams = {"name": "multicast-udp-tibrv://devilsMind;239.69.69.69"}
## if the transport already exist according the name the rest service return the existing transport
r = s.get(srvurl + 'Ariane/rest/mapping/domain/transports/create', params=transportParams)
transportID = r.json().get('transportID')

linkParams = {"SEPID":endpointID,"TEPID":0,"transportID":transportID}
r = s.get(srvurl + 'Ariane/rest/mapping/domain/links/create', params=linkParams)