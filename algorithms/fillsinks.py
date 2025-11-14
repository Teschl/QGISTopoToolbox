import os

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessingAlgorithm, 
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterRasterDestination,
                       QgsProcessingException)
from qgis.PyQt.QtGui import QIcon

import topotoolbox as tt

# Import topotoolbox from wheels if not installed in OSGeo4W Shell
# linux https://stackoverflow.com/questions/64008273/how-can-i-install-a-third-party-python-library-for-example-pandas-in-qgis-on-l

# https://gis.stackexchange.com/questions/311726/adding-missing-python-packages-to-qgis-plugin

class Fillsinks(QgsProcessingAlgorithm):
    INPUT_RASTER = 'INPUT_RASTER'
    HYBRID = 'HYBRID'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)
    def createInstance(self):
        return Fillsinks()
    def name(self):
        return 'fillsinks'
    def displayName(self):
        return self.tr('Fillsinks')
    def group(self):
        return self.tr('GridObject')
    def groupId(self):
        return 'gridobject'
    def shortHelpString(self):
        return self.tr("Fills sinks in a DEM using topotoolbox's fillsinks method")
    def icon(self):
        return QIcon(os.path.join(os.path.dirname(__file__), 'icons', 'fillsinks.png'))
    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT_RASTER,
                self.tr('Input DEM raster')
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.HYBRID,
                self.tr('Use hybrid reconstruction algorithm'),
                defaultValue=True
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterDestination(
                self.OUTPUT,
                self.tr('Filled DEM')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_raster = self.parameterAsRasterLayer(parameters, self.INPUT_RASTER, context)
        use_hybrid = self.parameterAsBool(parameters, self.HYBRID, context)
        if input_raster is None:
            raise QgsProcessingException("Invalid input raster layer")

        input_path = input_raster.source()
        dem = tt.read_tif(input_path)
        filled_dem = dem.fillsinks(hybrid=use_hybrid)

        output_path = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)
        tt.write_tif(filled_dem, output_path)

        # placeholder for linux:
        # output_path = input_path

        return {self.OUTPUT: output_path}