# Performance Evaluations of Cellular V2X

This project we explore the reliability of Mode 4 mechanisms via two parameters: **resource selection window length** and **vehicle density**. 
To do so, we used the Simulation of Urban Mobility (SUMO) to create a sample traffic network, and ms-van3t to observe vehicular communications 
under two V2X architectures: IEEE 802.11p and 3GPP C-V2X. 

## Installing SUMO

Eclipse SUMO (Simulation of Urban MObility) is an open source multi-modal traffic simulation package designed to handle large networks.

* Follow the guide at [https://sumo.dlr.de/wiki/Downloads](https://sumo.dlr.de/wiki/Downloads)
    * You may use:

    	`sudo add-apt-repository ppa:sumo/stable`  
    	`sudo apt update`  
    	`sudo apt install sumo sumo-tools sumo-doc`
      
## Installing ms-van3t

ms-van3t is an open-source tool based in SUMO (v1.6.0+) and ns-3 (v3.33) to simulate ETSI-compliant V2X applications.
    
* Clone the ms-van3t repository:
`git clone https://github.com/marcomali/ms-van3t`

* From this repository, run: `./sandbox_builder.sh`
   
* Configure `waf` to build the framework: `<ns3-folder>./waf configure --build-profile=optimized --enable-examples --enable-tests"`

* Build ns3: `./waf build`

## Acknowledgements

<a id="1">[1]</a> [Eclipse SUMO](https://www.eclipse.org/sumo/)

<a id="2">[2]</a> ["A Multi-stack Simulation Framework for Vehicular Applications Testing"](https://doi.org/10.1145/3416014.3424603)
