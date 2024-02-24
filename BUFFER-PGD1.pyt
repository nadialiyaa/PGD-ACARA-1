import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Buffer ToolBox"
        self.alias = "Buffer"

        # List of tool classes associated with this toolbox
        self.tools = [Buffer_pts]


class Buffer_pts(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool Buffer Points"
        self.description = "This Python Script Will Buffer Points"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter()
        param0.name = "Parameter0"
        param0.displayName = "Input Class Feature:"
        param0.parameterType = "Required"
        param0.direction = "Input"
        param0.datatype = "Feature Layer"
        param0.filter.list = ["Point"]

        param1 = arcpy.Parameter()
        param1.name = "Parameter1"
        param1.displayName = "Input Buffer Distance:"
        param1.parameterType = "Required"
        param1.direction = "Input"
        param1.datatype = "Long"

        return [param0,param1]
##
##    def isLicensed(self):
##        """Set whether tool is licensed to execute."""
##        return True
##
##    def updateParameters(self, parameters):
##        """Modify the values and properties of parameters before internal
##        validation is performed.  This method is called whenever a parameter
##        has been changed."""
##        return
##
##    def updateMessages(self, parameters):
##        """Modify the messages created by internal validation for each tool
##        parameter.  This method is called after internal validation."""
##        return
##
    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_FC = parameters[0].valueAsText
        buf_dist = parameters[1].valueAsText

        messages.addMessage("INPUT FEATURE CLASS = " + input_FC)
        messages.addMessage("BUFFER DISTANCE = " + buf_dist)
        
        import os
        name = arcpy.Describe(input_FC).basename + "_buf" + buf_dist
        path = arcpy.Describe(input_FC).path
        output_FC = os.path.join (path,name)

        #ADD BUFFER
        messages.addMessage ("BUFFERING..." + input_FC + buf_dist)
        arcpy.Buffer_analysis(input_FC, output_FC, buf_dist)
        return
