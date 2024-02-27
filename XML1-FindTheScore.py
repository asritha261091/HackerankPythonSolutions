import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    attrNumber=0
    for child in node.iter():
        attrNumber+=len(child.attrib.keys())
    return attrNumber
            
    # your code goes here

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
