import os

# pylint: disable=import-error
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessingAlgorithm,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterRasterDestination,
                       QgsProcessingException)
from qgis.PyQt.QtGui import QIcon

# Import topotoolbox, has to be installed in OSGeo4W Shell (Windows)
# 1. Open OSGeo4W Shell
# 2. Run: pip install topotoolbox
# Not jet working on Linux (and MacOS) due to missing OSGeo4W Shell
import topotoolbox as tt

class Excesstopgraphy(QgsProcessingAlgorithm):
    INPUT_RASTER = 'INPUT_RASTER'
    METHOD = 'METHOD'
    THRESHOLD = 'THRESHOLD'
    OUTPUT = 'OUTPUT'

    def createInstance(self):
        return Excesstopgraphy()

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def name(self):
        return 'excesstopgraphy'

    def displayName(self):
        return self.tr('Excesstopgraphy')
    
    def shortHelpString(self):
        return self.tr("")

    def icon(self):
        return QIcon(os.path.join(os.path.dirname(__file__), 'icons', 'excesstopgraphy.png'))

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT_RASTER,
                self.tr('Input DEM')
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.METHOD,
                'Calculation method',
                options=['fsm2d', 'fmm2d'],
                defaultValue='fsm2d',
                optional=False
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.THRESHOLD,
                self.tr('Threshold for excess topography calculation'),
                defaultValue=0.2
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterDestination(
                self.OUTPUT,
                self.tr('')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_raster = self.parameterAsRasterLayer(parameters, self.INPUT_RASTER, context)
        threshold = self.parameterAsNumber(parameters, self.THRESHOLD, context)
        method = self.parameterAsEnum(parameters, self.METHOD, context)

        if input_raster is None:
            raise QgsProcessingException("Invalid input raster layer")

        input_path = input_raster.source()
        dem = tt.read_tif(input_path)

        if method == 0:
            method = 'fsm2d'
        else:
            method = 'fmm2d'

        result_dem = dem.excesstopography(threshold=threshold, method=method)

        output_path = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)
        tt.write_tif(result_dem, output_path)
        return {self.OUTPUT: output_path}
