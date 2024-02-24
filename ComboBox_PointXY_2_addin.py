import arcpy
import pythonaddins

class ComboBoxClass1(object):
    """Implementation for ComboBox_PointXY_2_addin.combobox (ComboBox)"""
    def __init__(self):
        self.editable = True
        self.enabled = True
        self.dropdownWidth = '1234567890123456789012345678901234567890'
        self.width = ''
    def onSelChange(self, selection):
        print"New Selection:",selection
        arcpy.AddXY_management(selection)
    def onEditChange(self, text):
        #print"Edit Change:",text
        pass
    def onFocus(self, focused):
        if focused:
                self.mxd = arcpy.mapping.MapDocument('current')
                layers = arcpy.mapping.ListLayers(self.mxd)
                self.items = []
                for layer in layers:
                    if layer.isFeatureLayer:
                        if(arcpy.Describe(layer).shapeType=="Point"):
                            self.items.append(layer.name)
                            print"Adding choice:",layer.name
    def onEnter(self):
        print"Current Value:",self.value
    def refresh(self):
        pass
