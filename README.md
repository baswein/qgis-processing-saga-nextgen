# QGIS Processing SAGA next gen provider
## About
A QGIS plugin that allows you to run [SAGA GIS](https://sourceforge.net/projects/saga-gis/
) tools from the QGIS processing toolbox. 
## Installation
To install the plugin search for **Processing Saga NextGen Provider** in the plugin manager in QGIS and press the install button. [Instructions](https://docs.qgis.org/latest/en/docs/training_manual/qgis_plugins/fetching_plugins.html
)
If SAGA is not already on your system install a version from the [SAGA downloads page](https://sourceforge.net/projects/saga-gis/files/">https://sourceforge.net/projects/saga-gis/files/) or using the osgeo4w installer. This plugin is tested on SAGA 9.2, 9.12 only but should work fine on more recent releases. If you don't want to fully install SAGA unzipping the SAGA folder to a location of your choice should work.
Then in QGIS go to **Settings -> Options -> Processing -> Providers -> SAGANG** and point the SAGA folder to your unzipped folder containing the SAGA binaries. Hint: double click in the blank area next to the SAGA folder. If you installed SAGA in your applications on MAC the file path should be /Applications/SAGA.app/Contents/MacOS


## History

https://docs.qgis.org/latest/en/docs/training_manual/qgis_plugins/fetching_plugins.html
https://sourceforge.net/projects/saga-gis/
In order to use SAGA tools in QGIS you need to install this plugin first, and then manually install SAGA 9.2.0 (or later). To install SAGA visit: "https://sourceforge.net/projects/saga-gis/files/". This plugin is tested on SAGA 9.2, 9.12 only. It may work for more recent releases. After downloading SAGA, unzip the folder or install SAGA. Then in QGIS go to **Settings -> Options -> Processing -> Providers -> SAGANG** and point the SAGA folder to your unzipped folder containing the SAGA binaries. 
Processing provider for SAGA 9.2 and above. Requires manual installation of SAGA binaries.</p>
    <p>Since QGIS 3.30 SAGA tools are not included in the standard QGIS installation. In order to use SAGA
    tools in QGIS you need to install this plugin first, and then manually install SAGA 9.2.0 (or later).</p>
    <p>To install SAGA visit: <a href="https://sourceforge.net/projects/saga-gis/files/">https://sourceforge.net/projects/saga-gis/files/</a>.
    This plugin is tested on SAGA 9.2, 9.12 only. It may work for more recent releases.</p>
    <p>After downloading SAGA, unzip the folder. Then in QGIS go to
    Settings -> Options -> Processing -> Providers -> SAGANG and point the SAGA folder to your unzipped folder
    containing the SAGA binaries.</p>
    </p>This code was originally in QGIS core but was split out as a plugin by North Road. 
    Baswein took it over for version 1.2.0 to make it availble for QGIS 4 and beyond. 
    Thank you to everyone who worked on this code over the years. The plugin is ment to be a bulk connection to SAGA and
    all tools may not work fully.</p>

[![Build Status](https://travis-ci.org/north-road/qgis-processing-saga-nextgen.svg?branch=master)](https://travis-ci.org/north-road/qgis-processing-r)

Processing SAGA Provider Plugin for SAGA 9.2.0

SAGA nowadays comes with an Interface Creator for QGIS. To use it compile SAGA with

-DWITH_DEV_TOOLS:BOOL=ON

and run

saga_cmd dev_tools 7




