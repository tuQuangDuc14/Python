class ThoNV:
    def __init__(self):
        pass
    def run(self):

        with open("temple.xml","r") as file:
            XML_data = file.read()
        XML_data = XML_data.replace("NAME","Tu Quang Duc")
        XML_data = XML_data.replace("TQD","23")

        with open("New_XML_File.xml", "w+") as file:
            file.write(XML_data) 
if __name__ == '__main__':
    ThoNV().run()