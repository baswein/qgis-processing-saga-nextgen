# QGIS Processing SAGA next gen provider
## About
A QGIS plugin that allows you to run [SAGA GIS](https://sourceforge.net/projects/saga-gis/
) tools from the QGIS processing toolbox. The plugin is a bulk connection to SAGA and all tools may not work fully.
## Installation
### Install Plugin
To install the plugin search for **Processing Saga NextGen Provider** in the plugin manager in QGIS and press the install button. [Instructions](https://docs.qgis.org/latest/en/docs/training_manual/qgis_plugins/fetching_plugins.html 
). Or install from zip using the zip file from the github repository releases section. 
### Install SAGA
If SAGA is not already on your system install a version from the [SAGA downloads page](https://sourceforge.net/projects/saga-gis/files/) or using the osgeo4w installer. This plugin is tested on SAGA 9.2, 9.10, and 9.14. If you don't want to fully install SAGA unzipping the SAGA folder to a location of your choice should work.
### Connect QGIS to SAGA
Then in QGIS go to **Settings -> Options -> Processing -> Providers -> SAGANG** and point the SAGA folder to your unzipped folder containing the SAGA binaries. Hint: double click in the blank area next to the SAGA folder. Once you have the path click outside of the box before pressing ok otherwise it might not take.  
If you installed SAGA in your applications on MAC the file path should be /Applications/SAGA.app/Contents/MacOS . 
On Windows using osgeo4w: C:\Users\your user name\AppData\Local\Programs\OSGeo4W\apps\saga

## Known Issues
### macOS: SAGA Dock icon appears when running tools (SAGA 9.14+)
Starting with SAGA 9.12, the macOS application icon for SAGA appears briefly in the Dock while processing tools are running. This is a SAGA upstream issue. A bug report has been filed with the SAGA project. The issue is cosmetic and does not affect tool execution or results.

## History
This was originally part of the SEXTANTE plugin by Victor Olaya before becoming part of QGIS core until QGIS version 3.30 when it was split out as a plugin by North Road. Baswein took it over for plugin version 1.2.0 to make it available for QGIS 4 and beyond. Thank you to everyone who worked on this code over the years and the QGIS and SAGA developers for their amazing work. 
