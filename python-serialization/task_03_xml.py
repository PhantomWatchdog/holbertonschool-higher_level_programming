#!/usr/bin/env python3
"""
03-xml.py
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize_to_xml
    serializes a dictionary to XML
    """
    root = ET.Element("root")
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    deserialize_from_xml
    deserializes an XML file to a dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
