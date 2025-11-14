def classFactory(iface):
    """Load TopoToolbox plugin."""
    
    # Check if topotoolbox package is installed and abort loading if not
    from qgis.PyQt.QtWidgets import QMessageBox
    try:
        __import__("topotoolbox")
    except ImportError:
        QMessageBox.warning(
            None,
            "Missing Python Package: 'topotoolbox'"
        )
        # returning None causes Error in QGIS but loading dummy plugin 
        # installs a placeholder instead of aborting installation. This 
        # placeholder has to be removed manually later.
        # TODO: decide which is better option
        class DummyPlugin:
            def initGui(self): pass
            def unload(self): pass
            
        # return None
        return DummyPlugin()
        
    from .topotoolboxplugin import TopoToolboxPlugin
    return TopoToolboxPlugin(iface)
