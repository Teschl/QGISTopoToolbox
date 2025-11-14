def classFactory(iface):
    """Load TopoToolbox plugin."""
    
    from qgis.PyQt.QtWidgets import QMessageBox
    try:
        __import__("topotoolbox")
    except ImportError:
        QMessageBox.warning(
            None,
            "Missing Python Packages",
            f"The topotoolbox package is required for the TopoToolbox plugin ",
            "to work in QGIS but has to be installed manually.\n",
            "on Windows (using the OSGeo4W Shell):\n"
            f"    pip install topotoolbox"
            "on Linux:\n"
            f"    pip install --user topotoolbox"
            "Then try to install the plugin again."
        )
        # returning None causes Error in QGIS but loading dummy plugin 
        # installs a placeholder instead of aborting installation. This 
        # placeholder has to be removed manually later.
        # TODO: decide which is better option
        
        # return None
        class DummyPlugin:
            def initGui(self): pass
            def unload(self): pass

        return DummyPlugin()
        
    from .topotoolboxplugin import TopoToolboxPlugin
    return TopoToolboxPlugin(iface)
