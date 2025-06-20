from qgis.core import QgsProject
from qgis.PyQt.QtWidgets import QMessageBox, QAction
import matplotlib.pyplot as plt
import os
import sys


class TopoToolboxPlugin:
    def __init__(self, iface):
        self.iface = iface

        # https://gis.stackexchange.com/questions/196002/
        # development-of-a-plugin-which-depends-on-an-external-python-library
        try:
            import topotoolbox as tt3
        except ImportError:
            this_dir = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(this_dir, "wheels", "topotoolbox-0.0.4-cp312-cp312-win_amd64.whl")
            sys.path.append(path)
            import topotoolbox as tt3
        
        QMessageBox.information(None, "Success", "TopoToolbox imported successfully!")
    
    def initGui(self):
        """Required QGIS plugin method to initialize GUI elements"""
        self.action = QAction("Test TopoToolbox", self.iface.mainWindow())
        self.iface.addPluginToMenu("TopoToolbox", self.action)
    
    def unload(self):
        """Required QGIS plugin method to clean up"""
        self.iface.removePluginMenu("TopoToolbox", self.action)