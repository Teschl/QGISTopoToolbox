def classFactory(iface):
    """Load TopoToolbox plugin."""
    from .topotoolboxplugin import TopoToolboxPlugin
    return TopoToolboxPlugin(iface)
