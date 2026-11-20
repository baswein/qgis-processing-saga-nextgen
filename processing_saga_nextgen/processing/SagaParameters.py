"""
***************************************************************************
    SagaParameters.py
    ---------------------
    Date                 : December 2018
    Copyright            : (C) 2018 by Nyall Dawson
    Email                : nyall dot dawson at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

import pathlib

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    Qgis,
    QgsProcessingParameterBoolean,
    QgsProcessingParameterEnum,
    QgsProcessingParameterExtent,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterField,
    QgsProcessingParameterFile,
    QgsProcessingParameterMatrix,
    QgsProcessingParameterMultipleLayers,
    QgsProcessingParameterNumber,
    QgsProcessingParameterPointCloudDestination,
    QgsProcessingParameterPointCloudLayer,
    QgsProcessingParameterRasterDestination,
    QgsProcessingParameterRasterLayer,
    QgsProcessingParameterString,
    QgsProcessingParameterVectorDestination,
    QgsProcessingParameters,
)

NUMBER_TYPE_INTEGER = getattr(
    getattr(Qgis, "ProcessingNumberParameterType", None), "Integer", 0
)
NUMBER_TYPE_DOUBLE = getattr(
    getattr(Qgis, "ProcessingNumberParameterType", None), "Double", 1
)

FILE_BEHAVIOR_FILE = getattr(
    getattr(Qgis, "ProcessingFileParameterBehavior", None), "File", 0
)
FILE_BEHAVIOR_FOLDER = getattr(
    getattr(Qgis, "ProcessingFileParameterBehavior", None), "Folder", 1
)

SOURCE_TYPE_MAP = {
    -2: getattr(getattr(Qgis, "ProcessingSourceType", None), "MapLayer", -2),
    -1: getattr(
        getattr(Qgis, "ProcessingSourceType", None), "VectorAnyGeometry", -1
    ),
    0: getattr(getattr(Qgis, "ProcessingSourceType", None), "VectorPoint", 0),
    1: getattr(getattr(Qgis, "ProcessingSourceType", None), "VectorLine", 1),
    2: getattr(getattr(Qgis, "ProcessingSourceType", None), "VectorPolygon", 2),
    3: getattr(getattr(Qgis, "ProcessingSourceType", None), "Raster", 3),
    4: getattr(getattr(Qgis, "ProcessingSourceType", None), "File", 4),
    5: getattr(getattr(Qgis, "ProcessingSourceType", None), "Vector", 5),
}

FIELD_TYPE_MAP = {
    -1: getattr(
        getattr(Qgis, "ProcessingFieldParameterDataType", None), "Any", -1
    ),
    0: getattr(
        getattr(Qgis, "ProcessingFieldParameterDataType", None), "Numeric", 0
    ),
    1: getattr(
        getattr(Qgis, "ProcessingFieldParameterDataType", None), "String", 1
    ),
    2: getattr(
        getattr(Qgis, "ProcessingFieldParameterDataType", None), "DateTime", 2
    ),
    3: getattr(
        getattr(Qgis, "ProcessingFieldParameterDataType", None), "Binary", 3
    ),
    4: getattr(
        getattr(Qgis, "ProcessingFieldParameterDataType", None), "Boolean", 4
    ),
}


def getParameterFromString(line, context=""):
    tokens = line.strip().split("|")
    param_type = tokens[0].lstrip("*")
    name = tokens[1]
    desc = tokens[2]

    param = None
    if param_type == "QgsProcessingParameterBoolean":
        default = (
            tokens[3].lower() == "true"
            if len(tokens) > 3 and tokens[3] != "None"
            else False
        )
        optional = tokens[4].lower() == "true" if len(tokens) > 4 else False
        param = QgsProcessingParameterBoolean(
            name, desc, defaultValue=default, optional=optional
        )

    elif param_type == "QgsProcessingParameterEnum":
        options = (
            tokens[3].split(";") if len(tokens) > 3 and tokens[3] != "None" else []
        )
        allow_multiple = tokens[4].lower() == "true" if len(tokens) > 4 else False
        default = int(tokens[5]) if len(tokens) > 5 and tokens[5] != "None" else None
        optional = tokens[6].lower() == "true" if len(tokens) > 6 else False
        param = QgsProcessingParameterEnum(
            name,
            desc,
            options=options,
            allowMultiple=allow_multiple,
            defaultValue=default,
            optional=optional,
        )

    elif param_type == "QgsProcessingParameterExtent":
        default = tokens[3] if len(tokens) > 3 and tokens[3] != "None" else None
        optional = tokens[4].lower() == "true" if len(tokens) > 4 else False
        param = QgsProcessingParameterExtent(
            name, desc, defaultValue=default, optional=optional
        )

    elif param_type == "QgsProcessingParameterFeatureSource":
        types = (
            [int(tokens[3])]
            if len(tokens) > 3 and tokens[3] not in ("None", "-1")
            else [-1]
        )
        default = tokens[4] if len(tokens) > 4 and tokens[4] != "None" else None
        optional = tokens[5].lower() == "true" if len(tokens) > 5 else False
        param = QgsProcessingParameterFeatureSource(
            name, desc, types=types, defaultValue=default, optional=optional
        )

    elif param_type == "QgsProcessingParameterField":
        default = tokens[3] if len(tokens) > 3 and tokens[3] != "None" else None
        parent = tokens[4] if len(tokens) > 4 and tokens[4] != "None" else ""
        raw_type = int(tokens[5]) if len(tokens) > 5 and tokens[5] != "None" else -1
        data_type = FIELD_TYPE_MAP.get(raw_type, FIELD_TYPE_MAP[-1])
        allow_multiple = tokens[6].lower() == "true" if len(tokens) > 6 else False
        optional = tokens[7].lower() == "true" if len(tokens) > 7 else False
        param = QgsProcessingParameterField(
            name,
            desc,
            defaultValue=default,
            parentLayerParameterName=parent,
            type=data_type,
            allowMultiple=allow_multiple,
            optional=optional,
        )

    elif param_type == "QgsProcessingParameterFile":
        behavior = (
            FILE_BEHAVIOR_FOLDER
            if len(tokens) > 3 and "Folder" in tokens[3]
            else FILE_BEHAVIOR_FILE
        )
        default = tokens[4] if len(tokens) > 4 and tokens[4] != "None" else None
        optional = tokens[5].lower() == "true" if len(tokens) > 5 else False
        param = QgsProcessingParameterFile(
            name,
            desc,
            behavior=behavior,
            extension="",
            defaultValue=default,
            optional=optional,
        )

    elif param_type == "QgsProcessingParameterMatrix":
        rows = int(tokens[3]) if len(tokens) > 3 and tokens[3] != "None" else 0
        fixed = tokens[4].lower() == "true" if len(tokens) > 4 else False
        headers = (
            tokens[5].split(";") if len(tokens) > 5 and tokens[5] != "None" else []
        )
        default = (
            tokens[6].split(",")
            if len(tokens) > 6 and tokens[6] != "None"
            else None
        )
        optional = tokens[7].lower() == "true" if len(tokens) > 7 else False
        param = QgsProcessingParameterMatrix(
            name,
            desc,
            numberRows=rows,
            hasFixedNumberRows=fixed,
            headers=headers,
            defaultValue=default,
            optional=optional,
        )

    elif param_type == "QgsProcessingParameterMultipleLayers":
        raw_type = (
            int(tokens[3]) if len(tokens) > 3 and tokens[3] != "None" else -1
        )
        layer_type = SOURCE_TYPE_MAP.get(raw_type, SOURCE_TYPE_MAP[-1])
        default = tokens[4] if len(tokens) > 4 and tokens[4] != "None" else None
        optional = tokens[5].lower() == "true" if len(tokens) > 5 else False
        param = QgsProcessingParameterMultipleLayers(
            name,
            desc,
            layerType=layer_type,
            defaultValue=default,
            optional=optional,
        )

    elif param_type == "QgsProcessingParameterNumber":
        is_int = len(tokens) > 3 and "Integer" in tokens[3]
        num_type = NUMBER_TYPE_INTEGER if is_int else NUMBER_TYPE_DOUBLE
        conv = int if is_int else float
        default = (
            conv(tokens[4]) if len(tokens) > 4 and tokens[4] != "None" else None
        )
        optional = tokens[5].lower() == "true" if len(tokens) > 5 else False
        param = QgsProcessingParameterNumber(
            name,
            desc,
            type=num_type,
            defaultValue=default,
            optional=optional,
        )
        if len(tokens) > 6 and tokens[6] != "None":
            param.setMinimum(conv(tokens[6]))
        if len(tokens) > 7 and tokens[7] != "None":
            param.setMaximum(conv(tokens[7]))

    elif param_type == "QgsProcessingParameterPointCloudDestination":
        default = tokens[3] if len(tokens) > 3 and tokens[3] != "None" else None
        optional = tokens[4].lower() == "true" if len(tokens) > 4 else False
        param = QgsProcessingParameterPointCloudDestination(
            name, desc, defaultValue=default, optional=optional
        )

    elif param_type == "QgsProcessingParameterPointCloudLayer":
        default = tokens[3] if len(tokens) > 3 and tokens[3] != "None" else None
        optional = tokens[4].lower() == "true" if len(tokens) > 4 else False
        param = QgsProcessingParameterPointCloudLayer(
            name, desc, defaultValue=default, optional=optional
        )

    elif param_type == "QgsProcessingParameterRasterDestination":
        default = tokens[3] if len(tokens) > 3 and tokens[3] != "None" else None
        optional = tokens[4].lower() == "true" if len(tokens) > 4 else False
        param = QgsProcessingParameterRasterDestination(
            name, desc, defaultValue=default, optional=optional
        )

    elif param_type == "QgsProcessingParameterRasterLayer":
        default = tokens[3] if len(tokens) > 3 and tokens[3] != "None" else None
        optional = tokens[4].lower() == "true" if len(tokens) > 4 else False
        param = QgsProcessingParameterRasterLayer(
            name, desc, defaultValue=default, optional=optional
        )

    elif param_type == "QgsProcessingParameterString":
        default = tokens[3] if len(tokens) > 3 and tokens[3] != "None" else None
        multi = tokens[4].lower() == "true" if len(tokens) > 4 else False
        optional = tokens[5].lower() == "true" if len(tokens) > 5 else False
        param = QgsProcessingParameterString(
            name,
            desc,
            defaultValue=default,
            multiLine=multi,
            optional=optional,
        )

    elif param_type == "QgsProcessingParameterVectorDestination":
        raw_type = (
            int(tokens[3]) if len(tokens) > 3 and tokens[3] != "None" else -1
        )
        src_type = SOURCE_TYPE_MAP.get(raw_type, SOURCE_TYPE_MAP[-1])
        default = (
            tokens[4] if len(tokens) > 4 and tokens[4] != "None" else None
        )
        optional = tokens[5].lower() == "true" if len(tokens) > 5 else False
        param = QgsProcessingParameterVectorDestination(
            name, desc, type=src_type, defaultValue=default, optional=optional
        )

    if param and context:
        param.setDescription(
            QCoreApplication.translate(context, param.description())
        )
    return param


class SagaImageOutputParam(QgsProcessingParameterRasterDestination):
    """
    Custom raster destination parameter for SAGA algorithms which create a raster image
    output, instead of SAGA's usual 'sdat' raster grid outputs.

    These outputs differ from the usual SAGA outputs and are always generated as TIF files instead
    of sdat.
    """

    # pylint: disable=missing-docstring

    def defaultFileExtension(self):
        return "tif"

    def supportedOutputRasterLayerExtensions(self):
        return ["tif"]

    def clone(self):
        copy = SagaImageOutputParam(self.name(), self.description())
        return copy

    def createFileFilter(self):
        return "{} (*.tif *.TIF)".format(
            QCoreApplication.translate("SAGAAlgorithm", "TIF files")
        )

    def isSupportedOutputValue(self, value, context):
        output_path = QgsProcessingParameters.parameterAsOutputLayer(
            self, value, context
        )
        if pathlib.Path(output_path).suffix.lower() != ".tif":
            return False, QCoreApplication.translate(
                "SAGAAlgorithm", "Output filename must use a .tif extension"
            )
        return True, ""

    # pylint: enable=missing-docstring


class Parameters:
    """
    Parameter utilities
    """

    @staticmethod
    def is_parameter_line(line):
        """
        Returns true if the given line corresponds to a SAGA parameter definition
        """
        return (
            line.startswith("SagaImageOutput")
            or line.startswith("QgsProcessingParameter")
            or line.startswith("Parameter")
            or line.startswith("*QgsProcessingParameter")
        )

    @staticmethod
    def create_parameter_from_line(line):
        """
        Creates a parameter from a definition line.
        """
        if not line.startswith("SagaImageOutput"):
            return getParameterFromString(line, "SAGAAlgorithm")
        tokens = line.split("|")
        params = [t if str(t) != str(None) else None for t in tokens[1:]]
        if len(params) > 3:
            params[3] = params[3].lower() == "true"
        if len(params) > 4:
            params[4] = params[4].lower() == "true"
        param = SagaImageOutputParam(*params)
        param.setDescription(
            QCoreApplication.translate("SAGAAlgorithm", param.description())
        )
        return param
