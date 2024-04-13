# lib parser
import argparse
# lib logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)

# Liệt kê các file và thư mục 
import glob
import os
from tool import OpenTool
from common import Common_Steps,StepStaus
from cfgxml import Test_xml

def Read_argument():
    # init parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="write args")
    # Options for tool
    parser.add_argument("-o", "--open", help="prepare generate compile execute report", nargs='+', default=None)
    return parser.parse_args()

class RunTool(Common_Steps):
    Mytest= None
    # chuws cacs bien khi init
    def __init__(self, open): 
        if open == "tresos":
            self.Open = open
        else:
            print("not")
        print("Init ok ")
        super().__init__(self.Open)

    def Start(self):
        self.Result = StepStaus.FAIL
        self.State = "Start"
        # import class khac 
        Test_xml().run()
        # ke thua
        self.LetStart()

        if self.Open == "tresos":
            print("---------------Loading...........")
            # OpenTool().run()
            self.Result = StepStaus.SUCCESSED #ca hai class kahc va ke thua
        else:
            self.Result = StepStaus.FAIL

        self.LetEnd()
        
if __name__ == '__main__':
    Argument = Read_argument()
    logging.info("open = %s",Argument.open[0])
    RunNew = RunTool(Argument.open[0])
    RunNew.Start()