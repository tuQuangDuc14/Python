import xml.etree.ElementTree as ET

class Test_xml():
    def __init__(self):
        tree = ET.parse('config.xml')
        root = tree.getroot()
        # print(root.tag) #Begin
        # print(root.attrib)
        # for i in root:
        #     print(i.tag, i.attrib)
        # print(root[0][0].text)
        self.User = root[0][0].text
        self.Age = root[0][1].text
        self.Company = root[0][2].text
    
    def run(self):
        print(self.User)
        print(self.Age)
        print(self.Company)


