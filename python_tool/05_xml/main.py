import xml.etree.ElementTree as ET

class Test_xml():
    def __init__(self):
        pass

    def run(self):
        tree = ET.parse('test.xml')
        root = tree.getroot()
        # print(root.tag) #Begin
        # print(root.attrib)
        for i in root:
            print(i.tag, i.attrib)

        print(root[0][0].text)
       




if __name__ == '__main__':
    Test_xml().run()