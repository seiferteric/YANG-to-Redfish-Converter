# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/YANG-to-Redfish-Converter/blob/master/LICENSE.md

types_mapping = {
    'binary': 'Edm.Binary',
    'bits': '',
    'boolean': 'Edm.Boolean',
    'decimal64': 'Edm.Decimal',
    'empty': '',
    'enumeration': 'Edm.EnumType',
    'identityref': 'Edm.String',
    'int8': 'Edm.Sbyte',
    'int16': 'Edm.Int16',
    'int32': 'Edm.Int32',
    'int64': 'Edm.Int64',
    'leafref': 'Edm.String',
    'string': 'Edm.String',
    'uint8': 'Edm.Byte',
    'uint16': 'RedfishYang.uint16',
    'uint32': 'RedfishYang.uint32',
    'uint64': 'RedfishYang.uint64',
    'union': '',
    'date-and-time': 'Edm.DateTimeOffset'
}

def get_node_types_mapping(node_type):
    """
    Return the CSDL mapping of the current YANG statement.
    :param node_type: YANG statment type
    :return The Redfish Node type in appropriate CSDL string format:
    """
    return 'RedfishYang.NodeTypes/' + node_type

property_mapping = {
    'argument': 'argument',
    'augment': 'augment',
    'base': 'base',
    'bits': 'bits',
    'case': 'case',
    'contact': 'contact',
    'choice': 'choice',
    'description': 'description',
    'deviation': 'deviation',
    'deviate': 'deviate',
    'error-message': 'error_message',
    'error-app-tag': 'error_app_tag',
    'extension': 'extension',
    'feature': 'feature',
    'iffeature': 'if_feature',
    'isxml': 'IsXml',
    'length': 'length',
    'min': 'min',
    'min-elements': 'min_elements',
    'max': 'max',
    'max-elements': 'max_elements',
    'must': 'must',
    'organization': 'organization',
    'ordered-by': 'ordered_by',
    'path': 'path',
    'presence': 'presence',
    'range': 'range',
    'reference': 'reference',
    'revision': 'revision',
    'status': 'status',
    'statement': 'statement',
    'units': 'units',
    'unique': 'unique',
    'when': 'when',
    'xmlblock': 'XmlBlock',
    'YangType': 'YangType',
    'yangversion': 'yang_version',
    'YinElement': 'yin'
}


def get_descriptive_properties_mapping(property_name):
    """
    Return the CSDL property mapping of the current YANG statement.
    :param node_type: YANG statment type
    :return The Redfish Node type in appropriate CSDL string format:
    """
    if property_name == 'description':
        return 'OData.Description'
    target_name = property_mapping.get(property_name, property_name)
    return 'RedfishYang.' + str(target_name)
