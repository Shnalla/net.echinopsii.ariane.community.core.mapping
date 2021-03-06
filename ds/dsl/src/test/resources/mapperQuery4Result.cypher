
START startContainer = node(*)
MATCH startContainer-[owns]->startContainerContainerPrimaryAdminGate
WHERE
startContainer.MappingGraphVertexType! = "container" AND
startContainerContainerPrimaryAdminGate.MappingGraphVertexID = startContainer.containerPrimaryAdminGate AND
(startContainerContainerPrimaryAdminGate.nodeName =~ ".*tibrvrdl03prd01.*")
WITH startContainer

START endEP = node(*)
WHERE
endEP.MappingGraphVertexType! = "endpoint" AND
(endEP.endpointURL = "multicast-udp-tibrv://tibrvrdl05prd01.lab01.dev.dekatonshivr.echinopsii.net/;239.69.69.69:6969")
WITH startContainer, endEP

MATCH path = startContainer -[:owns|link*]- endEP
WHERE
ALL(n in nodes(path) where 1=length(filter(m in nodes(path) : m=n))) AND
ALL(n in nodes(path) where n.MappingGraphVertexType <> "cluster")
RETURN DISTINCT
EXTRACT(co in FILTER( n in nodes(path): n.MappingGraphVertexType! = "container"): co.MappingGraphVertexID) as CID,
EXTRACT(no in FILTER( n in nodes(path): n.MappingGraphVertexType! = "node"): no.MappingGraphVertexID) as NID,
EXTRACT(e in FILTER( n in nodes(path): n.MappingGraphVertexType! = "endpoint"): e.MappingGraphVertexID) as EID,
EXTRACT(t in FILTER( n in nodes(path): n.MappingGraphVertexType! = "transport"): t.MappingGraphVertexID) as TID,
EXTRACT(l in FILTER( r in relationships(path) : type(r) = "link"): l.MappingGraphEdgeID) as LID;