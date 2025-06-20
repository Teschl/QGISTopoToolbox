# In QGIS Python console:
import sys

def classFactory(iface):
    from .topotoolbox import TopoToolboxPlugin
    return TopoToolboxPlugin(iface)

