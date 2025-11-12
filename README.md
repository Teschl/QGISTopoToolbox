# QGISTopoToolbox

## How to use

TODO

## Installing

1. Compress repository into a .zip file
2. Navigate to 'Plugins'->'Manage and install Plugins...'
3. Click on 'Install from ZIP'
4. Select the .zip file and click 'Install Plugin'

The installation will fail if the topotoolbox package is not installed and on the Python-Path of the QGIS installation. As of this moment there is no clean method to automatically install dependencies that are missing for plugins to work. [It's generally not wanted to install packages without properly handeling versioning as to not break any other plugins.](https://gis.stackexchange.com/questions/311726/adding-missing-python-packages-to-qgis-plugin) Some possible solutions have been discussed: [here](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/202#issuecomment-1997009497), [QPIP Plugin](https://plugins.qgis.org/plugins/a00_qpip/#plugin-details) or [here](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/202#issuecomment-815844271).
The QPIP plugin might be a good solution going forward, but it's still in the early stages of development.

### Installing the TopoToolbox Package in QGIS for Windows

1. Open the OSGeo4W Shell
2. Install the topotoolbox using: `pip install topotoolbox`

### Installing the TopoToolbox Package in QGIS for Linux

On Linux the TopoToolbox package has to be added to the Python-Path since QGIS is not using a standalone Python installation on Linux.

## Developer information

TODO

## More resources regarding installing external Packages

- [https://gis.stackexchange.com/questions/392713/plugin-development-for-qgis-3-16-windows-how-to-handle-dependencies-on-extern](https://gis.stackexchange.com/questions/392713/plugin-development-for-qgis-3-16-windows-how-to-handle-dependencies-on-extern)
- [https://github.com/ivanlonel/qgis-plugin-with-pip-dependencies](https://github.com/ivanlonel/qgis-plugin-with-pip-dependencies)
- [https://github.com/opengisch/qpip](https://github.com/opengisch/qpip)
- [https://gis.stackexchange.com/questions/468241/qgis-python-plugin-install-python-depencies](https://gis.stackexchange.com/questions/468241/qgis-python-plugin-install-python-depencies)
- [https://gis.stackexchange.com/questions/45585/what-is-the-osgeo4w-equivalent-for-linux](https://gis.stackexchange.com/questions/45585/what-is-the-osgeo4w-equivalent-for-linux)
- [https://stackoverflow.com/questions/64008273/how-can-i-install-a-third-party-python-library-for-example-pandas-in-qgis-on-l](https://stackoverflow.com/questions/64008273/how-can-i-install-a-third-party-python-library-for-example-pandas-in-qgis-on-l)
- [https://gis.stackexchange.com/questions/141320/installing-3rd-party-python-libraries-for-qgis-on-windows](https://gis.stackexchange.com/questions/141320/installing-3rd-party-python-libraries-for-qgis-on-windows)
- [https://gis.stackexchange.com/questions/311726/adding-missing-python-packages-to-qgis-plugin](https://gis.stackexchange.com/questions/311726/adding-missing-python-packages-to-qgis-plugin)
