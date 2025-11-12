from qgis.PyQt.QtWidgets import QAction
from qgis.core import (
    QgsProcessingAlgorithm,
    QgsProcessingParameterRasterLayer,
    QgsProcessingParameterNumber,
    QgsProcessingParameterRasterDestination,
    QgsProcessingException,
    QgsProcessingProvider,
    QgsApplication,
    QgsProcessingRegistry
)
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon
from .fillsinks import Fillsinks
import os
import sys


class TopoToolboxProvider(QgsProcessingProvider):
    def __init__(self):
        super().__init__()
    def loadAlgorithms(self):
        self.addAlgorithm(Fillsinks())
    def id(self):
        return 'topotoolbox'
    def name(self):
        return 'TopoToolbox'
    def icon(self):
        return QIcon(os.path.join(os.path.dirname(__file__), 'icons', 'logo.png'))

class TopoToolboxPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.provider = None
    def initProcessing(self):
        self.provider = TopoToolboxProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)
    def initGui(self):
        self.initProcessing()
    def unload(self):
        if self.provider:
            QgsApplication.processingRegistry().removeProvider(self.provider)
