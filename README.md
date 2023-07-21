# LocareJSON

LocareJSON is a collection of JSON schemas for defining geometrical shapes with coordinates in 3D brain atlas coordinate systems. The goal is to represent diverse neuroscientific data using normalized representations (point, sphere, line string, cylinder, polygon or polyhedron) for the purpose of co-visualization and to enable spatial queries. It is based on GeoJSON (https://github.com/geojson/geojson.github.io) but extended to accommodate for 3D elements. 



## Specifications
Here we list and describe the main properties of a LocareJSON file (see also examples).

_For all LocareJSON files:_
* version	(mandatory): LocareJSON version number, e.g. 1.0.0
* targetAtlas (mandatory): target 3D atlas space version 
  * commonCoordinateSpaceVersion: link to instance from openMINDS_SANDS (https://github.com/HumanBrainProject/openMINDS_SANDS)
  * coordinateSpaceSetup: details extracted from commonCoordinateSpaceVersion needed to interpret coordinates correctly
      * dimensions: dimensions of coordinate space given as list of xyz  
      * resolution: isotropic resolution, e.g. 25 μm
      * orientation: three letter annotation for anatomical coordinate system as described here https://www.slicer.org/wiki/Coordinate_systems", e.g. RAS
      * origin: coordinate space origin given as list of xyz, e.g. 0,0,0 
* sourcePublication	(mandatory): PID of original source of data, e.g. DOI of dataset or journal paper
* relatedPublications	(optional):	list of PIDs for related publications, e.g. DOI of journal paper or dataset 
*linkedURI (optional): URI associated to sourcePublication, e.g. direct link to viewer presenting relevant data

_For point, sphere, lineString, cylinder, polygon and polyhedron in LocareCollection:_		
* geometry (mandatory): defining a geometric object  
  * type (mandatory): Point, Sphere, LineString, Cylinder, Polygon or Polyhedron
  * coordinates (mandatory): list of xyz coordinates in chosen 3D atlas space, formatted depending on type of geometric object
* properties (mandatory): details connected to each geometric object representation
  * name (mandatory): name of data represented by geometric object, preferably clearly routing to a subject, a subset of files or a single file in the data repository of a dataset
  * description (mandatory): describing what the geometric object represents, e.g. position of cell body or position of a brain section image
  * linkedURI (optional): URI associated to specific geometric object, e.g. direct link to viewer presenting relevant data

_For atlasMesh in LocareCollection:_
* atlasMesh (mandatory): defining a specific atlas mesh
  * parcellationEntityVersion (mandatory): link to instance from openMINDS_SANDS
* properties (mandatory): details connected to each geometric object representation
  * name (mandatory): name of data associated to atlas mesh, preferably clearly routing to a subject, a subset of files or a single file in the data repository of a dataset
  * description (mandatory): describing what the atlas mesh is associated to, e.g. specific parts of a study and/or set of files
  * linkedURI (optional): URI associated to specific atlas mesh association, e.g. direct link to viewer presenting relevant data

## Contributing
Feel free to reach out, either by email (c.h.blixhavn@medisin.uio.no) or by raising an issue. Also, pull requests are welcome. 

## Acknowledgements
The LocareJSON project is created at the Neural Systems laboratory at the University of Oslo as part of contributions to EBRAINS (https://www.ebrains.eu/) and the Human Brain Project, funded from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under Specific Grant Agreements No. 720270, No. 785907, and No. 945539 (Human Brain Project SGA1, SGA2, and SGA3).

## License
LocareJSON is licensed under CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
