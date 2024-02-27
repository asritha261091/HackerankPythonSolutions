import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    childList=[]
    global maxdepth
    for child in elem.iter():
        if child:
            if child.tag not in childList:
                childList.append(child.tag)
                maxdepth+=1
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
