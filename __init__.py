def classFactory(iface):
    """Load TopoToolbox plugin."""

    # Check if topotoolbox package is installed and abort loading if not
    from qgis.PyQt.QtWidgets import QMessageBox

    try:
        __import__("topotoolbox")
    except ImportError:
        QMessageBox.warning(None, "Missing Python Package: 'topotoolbox'")
        return None

    from .topotoolboxplugin import TopoToolboxPlugin

    return TopoToolboxPlugin(iface)
